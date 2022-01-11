import pandas as pd

pd.set_option('display.max_columns', 8)
general = pd.read_csv('general.csv')
prenatal = pd.read_csv('prenatal.csv')
sports = pd.read_csv('sports.csv')

prenatal.rename(columns={'HOSPITAL': 'hospital', 'Sex': 'gender'}, inplace=True)

sports.rename(columns={'Hospital': 'hospital', 'Male/female': 'gender'}, inplace=True)

new_data = pd.concat([general, prenatal, sports], ignore_index=True)

new_data.drop(columns=['Unnamed: 0'], inplace=True)
print(new_data.sample(n=20, random_state=30))