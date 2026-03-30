from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.inference import VariableElimination
import pandas as pd

data = pd.DataFrame({
    'Rain': ['No','No','Yes','Yes','No','Yes','Yes','No'],
    'TrafficJam': ['Yes','No','Yes','No','Yes','Yes','No','No'],
    'ArriveLate': ['Yes','No','Yes','No','No','Yes','Yes','No']
})
model = DiscreteBayesianNetwork([
    ('Rain', 'TrafficJam'),
    ('TrafficJam', 'ArriveLate')
])
model.fit(data)
print(model.get_cpds())

inference = VariableElimination(model)
result = inference.query(
    variables=['ArriveLate'],
    evidence={'Rain': 'Yes'}
)
print(result)
