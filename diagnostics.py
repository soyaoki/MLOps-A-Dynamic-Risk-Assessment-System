
import pandas as pd
import numpy as np
import timeit
import os
import json
import pickle
import subprocess

##################Load config.json and get environment variables
with open('config.json','r') as f:
    config = json.load(f) 

##################Function to get model predictions
def model_predictions(model_path, test_data_path):
    #read the deployed model and a test dataset, calculate predictions
    model = pickle.load(open(os.path.join(model_path, 'trainedmodel.pkl'), 'rb'))
    
    df_test = pd.read_csv(os.path.join(test_data_path, 'testdata.csv'))
    X_test= df_test[['lastmonth_activity', 'lastyear_activity', 'number_of_employees']]
    y_test = df_test['exited']

    y_pred = model.predict(X_test)
    
    return y_pred #return value should be a list containing all predictions

##################Function to get summary statistics
def dataframe_summary(dataset_csv_path):
    #calculate summary statistics here
    df = pd.read_csv(os.path.join(dataset_csv_path, 'finaldata.csv'))
    return list(df.describe()) #return value should be a list containing all summary statistics

##################Function to check for missing data
def check_missing(dataset_csv_path):
    #count NA values and calculate rates of NA
    df = pd.read_csv(os.path.join(dataset_csv_path, 'finaldata.csv'))
    return list(df.isna().mean()) #return a list of rates of NA

##################Function to get timings
def execution_time():
    #calculate timing of training.py and ingestion.py
    execution_time = []
    
    time_start = timeit.default_timer()
    subprocess.run(['python', 'training.py'])
    time_end = timeit.default_timer()
    time_delta =time_end - time_start
    execution_time.append(time_delta)
    
    time_start = timeit.default_timer()
    subprocess.run(['python', 'ingestion.py'])
    time_end = timeit.default_timer()
    time_delta =time_end - time_start
    execution_time.append(time_delta)
    
    return execution_time #return a list of 2 timing values in seconds

##################Function to check dependencies
def outdated_packages_list():
    #get a list of outdated packages
    return subprocess.check_output(['python', '-m', 'pip', 'list', '--outdated']).decode()


if __name__ == '__main__':
    model_path = os.path.join(config['output_model_path']) 
    test_data_path = os.path.join(config['test_data_path']) 
    dataset_csv_path = os.path.join(config['output_folder_path']) 
    
    model_predictions(model_path, test_data_path)
    dataframe_summary(dataset_csv_path)
    check_missing(dataset_csv_path)
    execution_time()
    outdated_packages_list()





    
