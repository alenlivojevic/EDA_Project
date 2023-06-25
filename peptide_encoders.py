import numpy as np
import peptides

class PeptidePropertiesEncoder:
    def encode(self, sequences):
        groups = (
            ('A', 'C', 'G', 'S', 'T'),                                  # Tiny
            ('A', 'C', 'D', 'G', 'N', 'P', 'S', 'T', 'V'),              # Small 
            ('A', 'I', 'L', 'V'),                                       # Aliphatic
            ('F', 'H', 'W', 'Y'),                                       # Aromatic
            ('A', 'C', 'F', 'G', 'I', 'L', 'M', 'P', 'V', 'W', 'Y'),    # Non-polar
            ('D', 'E', 'H', 'K', 'N', 'Q', 'R', 'S', 'T'),              # Polar
            ('D', 'E', 'H', 'K', 'R'),                                  # Charged
            ('H', 'K', 'R'),                                            # Basic
            ('D', 'E')                                                  # Acidic
        )

        X = []
        for sequence in sequences:
            sequence = sequence.upper()

            peptide = peptides.Peptide(sequence)
            x = [
                peptide.cruciani_properties()[0],
                peptide.cruciani_properties()[1],
                peptide.cruciani_properties()[2],
                peptide.instability_index(),
                peptide.boman(),
                peptide.hydrophobicity("Eisenberg"),
                peptide.hydrophobic_moment(angle=100, window=min(len(sequence), 11)),
                peptide.aliphatic_index(),
                peptide.isoelectric_point("Lehninger"),
                peptide.charge(pH=7.4, pKscale="Lehninger"),
            ]

            # Count tiny, small, aliphatic, ..., basic and acidic amino acids
            for group in groups:
                count = 0
                for amino in group:
                    count += sequence.count(amino)
                x.append(count)
                x.append(count / len(sequence))
            X.append(x)
        return np.array(X)