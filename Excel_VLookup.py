import pandas as pd

data = {'ID': [100, 101, 102, 103, 104, 105, 106, 107],
        'Name': ['Ram', 'Kartik', 'Shivani', 'Nikita', 'Deepshika', 'Upmanyu', 'Rajvir', 'Prachi']}
df1 = pd.DataFrame(data)

lookup_data = {'ID': [102, 103, 106, 107],
               'Performance': ['Good', 'Best', 'Best', 'Good']}
df2 = pd.DataFrame(lookup_data)

# Perform VLOOKUP-like operation with handling missing values and a default value
default_value = 'N/A'  # Specify the default value for missing entries

result = pd.merge(df1, df2, on='ID', how='left')

# Fill missing entries with the default value
result['Performance'].fillna(default_value, inplace=True)

print(result)
