from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.inference import VariableElimination
import pandas as pd

# -----------------------------
# 1. Create Sample Data
# -----------------------------
data = pd.DataFrame({
    'Rain': ['No','No','Yes','Yes','No','Yes','Yes','No'],
    'TrafficJam': ['Yes','No','Yes','No','Yes','Yes','No','No'],
    'ArriveLate': ['Yes','No','Yes','No','No','Yes','Yes','No']
})

# -----------------------------
# 2. Define Network Structure
# Rain → TrafficJam → ArriveLate
# -----------------------------
model = DiscreteBayesianNetwork([
    ('Rain', 'TrafficJam'),
    ('TrafficJam', 'ArriveLate')
])

# -----------------------------
# 3. Train the Model
# -----------------------------
model.fit(data)

# -----------------------------
# 4. Print Learned Probabilities
# -----------------------------
print("Conditional Probability Tables (CPDs):\n")
for cpd in model.get_cpds():
    print(cpd)
    print()

# -----------------------------
# 5. Perform Inference
# -----------------------------
inference = VariableElimination(model)

# Query: Probability of ArriveLate when Rain = Yes
result = inference.query(
    variables=['ArriveLate'],
    evidence={'Rain': 'Yes'}
)

print("Query Result:\n")
print(result)