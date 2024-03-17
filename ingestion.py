import pandas as pd
import numpy as np
import os
import json
from datetime import datetime

import glob


#############Load config.json and get input and output paths
with open('config.json','r') as f:
    config = json.load(f) 

#############Function for data ingestion
def merge_multiple_dataframe(input_folder_path, output_folder_path):
    #check for datasets, compile them together, and write to an output file
    
    # Define dataframe
    df_compiled = pd.DataFrame([])
    
    # Get paths of CSV files
    csv_path_list = glob.glob(os.path.join(input_folder_path, '*.csv'))
    
    # Load each CSV file as dataframe
    for csv_path in csv_path_list:
        df = pd.read_csv(csv_path)
        df_compiled = df_compiled.append(df, ignore_index=True)
    
    # Drop duplicates
    df_compiled = df_compiled.drop_duplicates().reset_index(drop=True)
    
    # Save dataframe
    df_compiled.to_csv(os.path.join(output_folder_path, 'finaldata.csv'), index=False)
    
    # Save names of CSV files
    with open(os.path.join(output_folder_path, 'ingestedfiles.txt'), 'w') as f:
        f.write('\n'.join(csv_path_list))
    
if __name__ == '__main__':
    input_folder_path = config['input_folder_path']
    output_folder_path = config['output_folder_path']
    
    merge_multiple_dataframe(input_folder_path, output_folder_path)
