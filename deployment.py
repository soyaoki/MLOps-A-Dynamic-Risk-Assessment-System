import os
import json
import subprocess


##################Load config.json and correct path variable
with open('config.json','r') as f:
    config = json.load(f) 

model_path = os.path.join(config['output_model_path']) 
prod_deployment_path = os.path.join(config['prod_deployment_path']) 
dataset_csv_path = os.path.join(config['output_folder_path']) 

####################function for deployment
def deploy_model():
    #copy the latest pickle file, the latestscore.txt value, and the ingestfiles.txt file into the deployment directory
    subprocess.call(['cp', os.path.join(model_path, 'trainedmodel.pkl'), os.path.join(prod_deployment_path, 'trainedmodel.pkl')])
    subprocess.call(['cp', os.path.join(model_path, 'latestscore.txt'), os.path.join(prod_deployment_path, 'latestscore.txt')])
    subprocess.call(['cp', os.path.join(dataset_csv_path, 'ingestedfiles.txt'), os.path.join(prod_deployment_path, 'ingestedfiles.txt')])
    
if __name__ == '__main__':    
    deploy_model()
