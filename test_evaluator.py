from fitness_evaluator import FitnessEvaluator

# MLP model on avpdb dataset
fitness_evaluator = FitnessEvaluator(dataset="avpdb.csv", model_type="mlp")
fitness_evaluator.init()
output = fitness_evaluator.predict(["AAC", "ADDDDDC"])

#output = fitness_evaluator.predict(["WFPHWHMHHAWLHCHHYYWMFFWHWKYHYVFYKFIWYWFHYLCWH", "ADDDDDC"])
print(output)
 
# Seqprops model on avpdb dataset
#fitness_evaluator = FitnessEvaluator(dataset="avpdb.csv", model_type="seqprops")
#fitness_evaluator.init()
#output = fitness_evaluator.predict(["AAC", "ADDDDDC"])
#print(output)