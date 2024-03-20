from flask import Flask, session, jsonify, request
import pandas as pd
import numpy as np
import pickle
import json
import os

from diagnostics import model_predictions, dataframe_summary, check_missing, execution_time
from scoring import score_model


######################Set up variables for use in our script
app = Flask(__name__)
app.secret_key = '1652d576-484a-49fd-913a-6879acfa6ba4'

with open('config.json','r') as f:
    config = json.load(f) 

dataset_csv_path = os.path.join(config['output_folder_path']) 
model_path = os.path.join(config['output_model_path']) 
test_data_path = os.path.join(config['test_data_path']) 

prediction_model = pickle.load(open(os.path.join(model_path, 'trainedmodel.pkl'), 'rb'))


#######################Prediction Endpoint
@app.route("/prediction", methods=['POST','OPTIONS'])
def predict():        
    #call the prediction function you created in Step 3    
    return str(model_predictions()) + '\n' #add return value for prediction outputs

#######################Scoring Endpoint
@app.route("/scoring", methods=['GET','OPTIONS'])
def score():        
    #check the score of the deployed model
    return str(score_model()) + '\n' #add return value (a single F1 score number)

#######################Summary Statistics Endpoint
@app.route("/summarystats", methods=['GET','OPTIONS'])
def stats():        
    #check means, medians, and modes for each column
    print(dataframe_summary())
    return str(dataframe_summary()) + '\n' #return a list of all calculated summary statistics

#######################Diagnostics Endpoint
@app.route("/diagnostics", methods=['GET','OPTIONS'])
def diagnose():        
    #check timing and percent NA values
    exe_time = execution_time()
    p_na = check_missing()
    return str(exe_time) + '\n' + str(p_na) #add return value for all diagnostics

if __name__ == "__main__":    
    app.run(host='0.0.0.0', port=8000, debug=True, threaded=True)
