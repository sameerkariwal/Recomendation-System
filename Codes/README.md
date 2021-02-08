# Hybrid News Recommmendation Model
Through these modules, we are trying to learn how to create recommender systems and the different components and techniques involved.

## Datasets
The [datasets](data/) folder stores datasets that are used in these models. Two sources of data are taken as describe below:

    -platform_content.csv: This dataset contains details about the news articles shared in the platform. Attributes such as timestamp, url, title, article description, language (English: en or Portuguese: pt) and info of the user(author) who shared the article

    -consumer_transactions.csv: This data source contains user behaviour and transanctional data of user interactions on platform_content articles. Multiple interaction_types are recorded to understand user's engagement on the platform.

other csv's are artifacts from the models.
   
## Modules
The [modules](modules/) folder contains modules for data processing, exploratory data analysis(EDA) and evaluations.

#### 1. data processing
#### 2. EDA
#### 3. evaluations

## Models
The [models](models/) folder contains 4 different machine learning models to generate recommendations. To Understand in brief each of them,

#### 1. collaborative filtering model
#### 2. content based filtering model
#### 3. hybrid recommendation model
#### 4. transformers based content model

The outputs of 1 and 2 are feeded with weightages to 3 to generate final recommendations and evaluated on the below evaluation code.
Model 4 is taken to explain an another approach towards content recommendation models based on article text NLP and recent developments in transformers based apporoaches. 

## Evaluation
The [evaluations](modules/evaluations.ipynb) notebook helps to evaluate model's performance on two major evaluation metrics hit rate and recall.

## How to read or run this repository?

#### 1. make sure you have anaconda install, go to anaconda navigator and run jupyter lab from there, if not then if you have linux like cmd line and simply type [jupyter lab], after you have installed the jupyter lab by running requirements.sh file as [sh requirements.sh] 
#### 2. After launching jupyter lab/notbook, go to the folder where you have downloaded this repo. Look for data folder that contains the data csv used in the model(names as mentioned above).
#### 3. Start from modules/EDA.ipynb file to understand the datasets and exploratory data analysis done over it.
#### 4. Look for modules/data_processing.ipynb code to understand the data processing done over the code.
#### 5. modules/evaluations.ipynb contains the evaluations that are needed for the model. 
#### 6. In model directory, start with collaborative filtering model, then content based filtering and sentence embedding which is another content based(text) based model.
#### 7. In the end, look for hybrid recommendations model to aggregate the previous model for final recommendation generation and comparision.
#### Note: In case there is any import issue while importing other notebooks(happens sometimes) put all notebooks into one folder and change the import command for the respective notebooks.

```
For any queries:
Please connect with me at: 
Sumit Jain
sumitjain.bits@gmail.com
```