# Project Overview

## Background
Imagine that you're the Chief Data Scientist at a big company that has 10,000 corporate clients. Your company is extremely concerned about attrition risk: the risk that some of their clients will exit their contracts and decrease the company's revenue. They have a team of client managers who stay in contact with clients and try to convince them not to exit their contracts. However, the client management team is small, and they're not able to stay in close contact with all 10,000 clients.

The company needs you to create, deploy, and monitor a risk assessment ML model that will estimate the attrition risk of each of the company's 10,000 clients. If the model you create and deploy is accurate, it will enable the client managers to contact the clients with the highest risk and avoid losing clients and revenue.

Creating and deploying the model isn't the end of your work, though. Your industry is dynamic and constantly changing, and a model that was created a year or a month ago might not still be accurate today. Because of this, you need to set up regular monitoring of your model to ensure that it remains accurate and up-to-date. You'll set up processes and scripts to re-train, re-deploy, monitor, and report on your ML model, so that your company can get risk assessments that are as accurate as possible and minimize client attrition.

![Project: a dynamic risk assessment system](https://video.udacity-data.com/topher/2021/April/60870ec7_screen-shot-2021-04-26-at-9.33.10-am/screen-shot-2021-04-26-at-9.33.10-am.png)
Project: a dynamic risk assessment system

## Project Steps Overview
You'll complete the project by proceeding through 5 steps:
  1. __Data ingestion.__ Automatically check a database for new data that can be used for model training. Compile all training data to a training dataset and save it to persistent storage. Write metrics related to the completed data ingestion tasks to persistent storage.
  2. __Training, scoring, and deploying.__ Write scripts that train an ML model that predicts attrition risk, and score the model. Write the model and the scoring metrics to persistent storage.
  3. __Diagnostics.__ Determine and save summary statistics related to a dataset. Time the performance of model training and scoring scripts. Check for dependency changes and package updates.
  4. __Reporting.__ Automatically generate plots and documents that report on model metrics. Provide an API endpoint that can return model predictions and metrics.
  5. __Process Automation.__ Create a script and cron job that automatically run all previous steps at regular intervals.

## Getting Started
We've provided you with a starter (click [here](https://video.udacity-data.com/topher/2021/March/60412fe6_starter-file/starter-file.zip) to download) that contains template scripts for each of the project steps. The starter also contains fabricated datasets that you can use for model training.

### The Workspace
You'll complete the project in the Udacity Workspace, which you will find on the __Workspace__ page in the current project lesson. The workspace contains all the computing resources needed to complete the project.

Your workspace has eight locations you should be aware of:

- `/home/workspace`, the root directory. When you load your workspace, this is the location that will automatically load. This is also the location of many of your starter files.
- `/practicedata/`. This is a directory that contains some data you can use for practice.
- `/sourcedata/`. This is a directory that contains data that you'll load to train your models.
- `/ingesteddata/`. This is a directory that will contain the compiled datasets after your ingestion script.
- `/testdata/`. This directory contains data you can use for testing your models.
- `/models/`. This is a directory that will contain ML models that you create for production.
- `/practicemodels/`. This is a directory that will contain ML models that you create as practice.
- `/production_deployment/`. This is a directory that will contain your final, deployed models.

__Important notes about the workspace:__

Your files under the `/home/workspace/` directory are saved for you automatically. However, after a __30 minutes__ idle time (navigate away from the Workspace, tab not accessed, or simply closed, or laptop asleep, etc), your Workspace will go sleep. If you return after this period, your files will be restored to your most recent work, but you will lose the list of __open files__ or any __shell sessions__ you may have had running.

## Starter Files
There are many files in the starter: 10 Python scripts, one configuration file, one requirements file, and five datasets.

The following are the Python files that are in the starter files:

- __training.py__, a Python script meant to train an ML model
- __scoring.py__, a Python script meant to score an ML model
- __deployment.py__, a Python script meant to deploy a trained ML model
- __ingestion.py__, a Python script meant to ingest new data
- __diagnostics.py__, a Python script meant to measure model and data diagnostics
- __reporting.py__, a Python script meant to generate reports about model metrics
- __app.py__, a Python script meant to contain API endpoints
- __wsgi.py__, a Python script to help with API deployment
- __apicalls.py__, a Python script meant to call your API endpoints
- __fullprocess.py__, a script meant to determine whether a model needs to be re-deployed, and to call all other Python scripts when needed
The following are the datasets that are included in your starter files. Each of them is fabricated datasets that have information about hypothetical corporations.

__Note__: these data have been uploaded to your workspace as well

- dataset1.csv and dataset2.csv, found in `/practicedata/`
- dataset3.csv and dataset4.csv, found in `/sourcedata/`
- testdata.csv, found in `/testdata/`

The following are other files that are included in your starter files:

- requirements.txt, a text file and records the current versions of all the modules that your scripts use
- config.json, a data file that contains names of files that will be used for configuration of your ML Python scripts
