import pickle
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
from sklearn import metrics
import matplotlib.pyplot as plt
import seaborn as sns
import json
import os

from diagnostics import model_predictions


###############Load config.json and get path variables
with open('config.json','r') as f:
    config = json.load(f) 
 
model_path = os.path.join(config['output_model_path']) 
test_data_path = os.path.join(config['test_data_path']) 

##############Function for reporting
def score_model():
    #calculate a confusion matrix using the test data and the deployed model
    #write the confusion matrix to the workspace
    y_pred = model_predictions()
    y_test = pd.read_csv(os.path.join(test_data_path, 'testdata.csv'))['exited']
    
    fig = metrics.ConfusionMatrixDisplay(metrics.confusion_matrix(y_test, y_pred))
    fig.plot()
    plt.savefig(os.path.join(model_path, 'confusionmatrix.png'))

if __name__ == '__main__':    
    score_model()
