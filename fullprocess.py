import pandas as pd
import json
import os
import glob

from ingestion import *
from training import *
from scoring import *
from deployment import *
from diagnostics import *
from reporting import *

###################Load config.json and get path variables
with open('config.json','r') as f:
    config = json.load(f) 

input_folder_path = config['input_folder_path']
output_folder_path = config['output_folder_path']

model_path = os.path.join(config['output_model_path']) 
prod_deployment_path = os.path.join(config['prod_deployment_path']) 
dataset_csv_path = os.path.join(config['output_folder_path']) 
test_data_path = os.path.join(config['test_data_path']) 

##################Check and read new data
#first, read ingestedfiles.txt
with open(os.path.join(prod_deployment_path, 'ingestedfiles.txt'), 'r') as f:
    ingestedfiles = f.read().splitlines()
print(ingestedfiles)

#second, determine whether the source data folder has files that aren't listed in ingestedfiles.txt
csv_path_list = glob.glob(os.path.join(input_folder_path, '*.csv'))
print(csv_path_list)

flag_newdata = False
for csv_path in csv_path_list:
    if(csv_path not in ingestedfiles):
        flag_newdata = True

##################Deciding whether to proceed, part 1
#if you found new data, you should proceed. otherwise, do end the process here
if(flag_newdata):
    print("[INFO] There were new data files.")
    print("[INFO] Starting new files ingestion...")
    merge_multiple_dataframe()
else:
    print("[INFO] No New data. Process ends.")
    exit(0)

##################Checking for model drift
#check whether the score from the deployed model is different from the score from the model that uses the newest ingested data
model = pickle.load(open(os.path.join(prod_deployment_path, 'trainedmodel.pkl'), 'rb'))
df_new = pd.read_csv(os.path.join(dataset_csv_path, 'finaldata.csv'))
X_new= df_new[['lastmonth_activity', 'lastyear_activity', 'number_of_employees']]
y_new = df_new['exited']
y_pred = model.predict(X_new)
f1_score = metrics.f1_score(y_new, y_pred)
with open(os.path.join(model_path, 'latestscore.txt'), 'w') as f:
    f.write(str(f1_score))

##################Deciding whether to proceed, part 2
#if you found model drift, you should proceed. otherwise, do end the process here
with open(os.path.join(prod_deployment_path, 'latestscore.txt'), 'r') as f:
    f1_at_deploy = float(f.read())
    
with open(os.path.join(model_path, 'latestscore.txt'), 'r') as f:
    f1_now = float(f.read())

flag_model_drift = (f1_at_deploy >= f1_now)
if(flag_model_drift):
    print("[INFO] Model drift was detected.")
else:
    print("[INFO] No model drif. Process ends.")
    exit(0) 
    
##################Re-deployment
#if you found evidence for model drift, re-run the deployment.py script
print("[INFO] Re Training & Deploying...")
subprocess.call(['python', 'training.py'])
subprocess.call(['python', 'deployment.py'])

##################Diagnostics and reporting
#run diagnostics.py and reporting.py for the re-deployed model
print("[INFO] Re Diagnosing & Reporting...")
subprocess.call(['python', 'diagnostics.py'])
subprocess.call(['python', 'reporting.py'])






