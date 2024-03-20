import requests
import json
import os

#Specify a URL that resolves to your workspace
URL = "http://127.0.0.1:8000"

with open('config.json', 'r') as f:
    config = json.load(f)

#Call each API endpoint and store the responses
response1 = requests.post(URL + '/prediction').content #put an API call here
response2 = requests.get(URL + '/scoring').content #put an API call here
response3 = requests.get(URL + '/summarystats').content #put an API call here
response4 = requests.get(URL + '/diagnostics').content #put an API call here

#combine all API responses
responses = [response1, '\n', '\n', response2, '\n', '\n', response3, '\n', '\n', response4]#combine reponses here

#write the responses to your workspace
with open(os.path.join(config['output_model_path'], 'apireturns2.txt'), 'w') as f:
    f.write(str(responses))


