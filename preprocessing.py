import pandas as pd

# reading data and handling unknowns
df = pd.read_csv('income-data.csv', na_values={
        'Year of Record': ['#N/A'],
        'Gender': [0, '#N/A', 'unknown'],
        'Age': ['#N/A'],
        'Country': [],
        'Size of City': [],
        'Profession': ['#N/A'],
        'University Degree': [0, '#N/A'],
        'Wears Glasses': [],
        'Hair Color': [0, '#N/A', 'Unknown'],
        'Body Height [cm]': [],
        'Income in EUR': []
})

df['Gender'].fillna('other', inplace=True)
df['Profession'].fillna(method='ffill', inplace=True)
df['University Degree'].fillna(method='ffill', inplace=True)
df['Hair Color'].fillna(method='ffill', inplace=True)
df['Income in EUR'] = df['Income in EUR'].abs()

print(df.head())
