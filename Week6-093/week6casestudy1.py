import pandas as pd
from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.estimators import MaximumLikelihoodEstimator
from pgmpy.inference import VariableElimination

data = pd.DataFrame({
    'Fever': ['Yes','Yes','No','Yes','No','No','Yes','No'],
    'Cough': ['Yes','No','Yes','Yes','No','No','Yes','No'],
    'Flu': ['No','Yes','No','Yes','No','No','Yes','No']
})

model = DiscreteBayesianNetwork([
    ('Fever', 'Flu'),
    ('Cough', 'Flu')
])

model.fit(data, estimator=MaximumLikelihoodEstimator)

infer = VariableElimination(model)

result = infer.query(variables=['Flu'], evidence={'Fever': 'Yes', 'Cough': 'Yes'})

print(result)