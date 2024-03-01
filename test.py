import pandas as pd
from itertools import product

# Read the CSV file into a DataFrame
df = pd.read_csv('k8s_historical_states_discrete_concurrency-3_third.csv')

# Specify the column names
columns = ['replicas_1', 'replicas_2', 'replicas_3']

# Generate all possible combinations of values for the specified columns
all_combinations = list(product(range(1, 6), repeat=len(columns)))

# Extract existing combinations from the DataFrame
existing_combinations = df[columns].apply(tuple, axis=1).tolist()

# Filter out existing combinations
unique_combinations = [c for c in all_combinations if c not in existing_combinations]

# Print the unique combinations
for combination in unique_combinations:
    print('-'.join(map(str, combination)))