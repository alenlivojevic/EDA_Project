import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import models
import peptide_encoders
from tensorflow import keras
from sklearn.preprocessing import StandardScaler
from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split
from seqprops import SequentialPropertiesEncoder
import os

class FitnessEvaluator:
    def __init__(self, dataset="avpdb.csv", model_type="mlp"):
        assert(model_type == "mlp" or model_type == "seqprops")
        assert(dataset == "avpdb.csv" or dataset == "amp.csv")
        self.dataset = dataset
        self.model_type = model_type

    def init(self):
        # Load sequences from a CSV file
        data = pd.read_csv(f"datasets/{self.dataset}")

        sequences = data["sequence"].to_numpy()
        y = data["label"].to_numpy()

        # Determine the length of the longest sequence
        max_seq_len = 0
        for sequence in sequences:
            max_seq_len = max(len(sequence), max_seq_len)

        # Shuffle data
        sequences, y = shuffle(sequences, y, random_state=42)
        sequences_train, sequences_val, y_train, y_val = train_test_split(sequences, y, test_size=0.2, random_state=42)

        # Converting peptide sequences to suitable representation
        if self.model_type == "mlp":
            self.encoder = peptide_encoders.PeptidePropertiesEncoder()
            X_train = self.encoder.encode(sequences_train)
            X_val = self.encoder.encode(sequences_val)
            self.scaler = StandardScaler()
            X_train = self.scaler.fit_transform(X_train)
            X_val = self.scaler.transform(X_val)
            self.model = models.create_mlp_model(input_shape=(28,), dense1_units=120, dense2_units=80, dense3_units=80)
        elif self.model_type == "seqprops":
            if self.dataset == "avpdb.csv":
                optimal_features = [
                    'Hydrophobicity_Cid', 'Hydrophobicity_Wolfenden', 'stScales_ST5', 
                    'Hydrophobicity_BullBreese', 'ProtFP_ProtFP5', 'BLOSUM_BLOSUM9', 
                    'Hydrophobicity_Casari', 'Hydrophobicity_KyteDoolittle', 
                    'stScales_ST8', 'tScales_T4'
                ] 
            elif self.dataset == "amp.csv":
                optimal_features = [
                    'Hydrophobicity_Fasman', 'tScales_T3', 'BLOSUM_BLOSUM5', 'BLOSUM_BLOSUM4', 
                    'Hydrophobicity_Aboderin', 'stScales_ST4', 'zScales_Z1', 'Hydrophobicity_Juretic', 
                    'ProtFP_ProtFP5', 'tScales_T5', 'MSWHIM_MSWHIM3'
                ]
            self.encoder = SequentialPropertiesEncoder(scaler=MinMaxScaler(feature_range=(-1, 1)), selected_properties=optimal_features, max_seq_len=51, stop_signal=True)
            X_train = self.encoder.encode(sequences_train)
            X_val = self.encoder.encode(sequences_val)
            self.model = models.create_seq_model(input_shape=X_train.shape[1:], conv1_filters=64, conv2_filters=64, conv_kernel_size=4, num_cells=128, dropout=0.1)


        # Check if pretrained model is available for selected combination of dataset and model type
        model_name = f"{self.model_type}_{self.dataset.split('.')[0]}"
        if os.path.exists(model_name):
            # Load model from disk
            self.model = keras.models.load_model(model_name)
        else:
            # Train model from scratch
            adam_optimizer = keras.optimizers.Adam(learning_rate=0.0001)
            early_stopping_callback = keras.callbacks.EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True)
            self.model.compile(loss="binary_crossentropy", optimizer=adam_optimizer)
            self.model.fit(X_train, y_train, validation_data=(X_val, y_val), epochs=200, batch_size=32, callbacks=[early_stopping_callback], verbose=1)

            # Save model to disk
            self.model.save(model_name)

    def predict(self, lst_sequences):
        if self.model_type == "mlp":
            X = self.encoder.encode(lst_sequences)
            X = self.scaler.transform(X)
            y_pred = self.model.predict(X, batch_size=64, verbose=0)
        elif self.model_type == "seqprops":
            X = self.encoder.encode(lst_sequences)
            y_pred = self.model.predict(X, batch_size=64, verbose=0)
        return np.reshape(y_pred, (-1, ))
            
        