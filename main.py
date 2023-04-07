import pandas as pd
import os
from tqdm import tqdm

file_list = list()
df_list = list()
for root, dirs, files in os.walk('/home/user/moloko'):
    for file in files:
        if file.endswith('.csv'):
         file_list.append(os.path.join(root, file))
for file in tqdm(file_list):
    values = list()
    df = pd.read_csv(file, encoding="utf-8", on_bad_lines='skip', index_col=[0])
    conc = float(file.split(os.sep)[-1].split('_')[-2])
    antibiotic = file.split(os.sep)[-1].split('_')[0]
    values = list(df[df.columns[1]].values)
    values.append(antibiotic)
    values.append(conc)
    df_list.append(values)
    feature_names = list(df[df.columns[0]].values)
    feature_names.append('antibiotic')
    feature_names.append('concentration')
main_df = pd.DataFrame(data=df_list, columns=feature_names)
main_df.to_csv('result_milk.csv')
print('Hello worldd')



