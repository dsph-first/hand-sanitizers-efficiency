"""This module load data from the xls file and process it to make a dataframe which is used for the colony count graph"""

import pandas as  pd
import yaml
import numpy as np


def get_config(file_name):
   '''This is the configuaration file
    It takes the file name and returns the load data
   '''
   with open(file_name,'r', encoding = 'UTF-8') as stream:
      config = yaml.safe_load(stream)
   return config  

config = get_config('config.yaml')
df = pd.read_excel(config['data'])

# droping the Unnamed: 0 columns and setting the experiments_ID as the index
df.drop(columns=['Unnamed: 0'], inplace=True )
df.set_index('experiment ID',inplace = True)

df = df.dropna() #removing all the nan values from the dataframe

df = df.T # Transposing it so make the handsanitizer and coltrol experiments as a column and smaples as a row


df['HS1_S'] = df[['HS1-1','HS1-2','HS1-3']].mean(axis =1)  # Calculating the sample mean for each triplicate
df['HS1_C'] = df[df.columns[df.columns.str.contains('C_HS1-\d+')]].mean(axis=1) #Calculating the control mean for each triplicate

df_result= df[df.columns[-2:]].T
df_result['count'] = df_result.mean(axis=1)

# resetting the index to split it into two columns
# HS for handsanitizer, Sample_type for whether it is sample or control
# Dropped the experiemnt id columns to make it clean

df_result.reset_index(inplace=True)
df_result[['HS', 'Sample_type']] = df_result['experiment ID'].str.split('_', n =1, expand= True)
df_result.drop(columns='experiment ID', inplace= True)

#Replacing the HS1 With hand sanitizer name
df_result.loc[df_result['HS'].str.contains('HS1'),'HS'] ='Sagrotan'


#Calculated the std to make the error bar
df_result['Std']= df_result.iloc[:,:5].std(axis=1)

# Mappping the Sample_type as treated and control for visualization purpose
df_result['Sample_type'] = df_result['Sample_type'].map({'S': 'Treated', 'C': 'Control'})

# Calculating following this for creating a error bar
sample_size = df_result.shape[0]
df_result['SEM_mean'] = df_result['Std'] / np.sqrt(sample_size)  # calculated standard error of the mean (SEM)
df_result['lower_limit'] = df_result['SEM_mean'] * 0.025 # 95% CI lower limit is 0.025
df_result['upper_limit'] = df_result['SEM_mean'] * 0.975 # 95% CI upper limit is 0.097
df = df_result.sem('columns',numeric_only=True,)

# print(df_result[df_result['HS'] =='Sagrotan'])
# print(df_result)

def return_dataframe(hand_sanitizer):
   return df_result[df_result['HS'] == hand_sanitizer]









