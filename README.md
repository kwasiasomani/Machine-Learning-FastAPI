# Machine-Learning-FastAPI Sepsis 

The early prediction of sepsis is potentially life-saving, and we challenge participants to predict sepsis 6 hours before the clinical prediction of sepsis.
![image](https://github.com/kwasiasomani/Machine-Learning-FastAPI/assets/119458164/759c16c6-3e29-466b-9ce1-4ca96594d713)

# Abstract
Sepsis is a life-threatening condition with high mortality rates. Early detection and treatment are critical to improving outcomes

Sepsis occurs when chemicals released in the bloodstream to fight an infection trigger inflammation throughout the body. This can cause a cascade of changes that damage multiple organ systems, leading them to fail, sometimes even resulting in death.

The data for this project is in a csv format. The following describes the columns present in the data.

## Dataset Description 
| Column Name | Target | Description                                                                   |
| ----------- | ------ | ----------------------------------------------------------------------------- |
| ID          | N/A    | Unique number to represent patient ID                                         |
| PRG         | False  | Plasma glucose                                                                |
| PL          | False  | Blood Work Result-1 (mu U/ml)                                                 |
| PR          | False  | Blood Pressure (mm Hg)                                                        |
| SK          | False  | Blood Work Result-2 (mm)                                                      |
| TS          | False  | Blood Work Result-3 (mu U/ml)                                                 |
| M11         | False  | Body mass index (weight in kg/(height in m)^2                                 |
| BD2         | False  | Blood Work Result-4 (mu U/ml)                                                 |
| Age         | False  | patients age (years)                                                          |
| Insurance   | N/A    | If a patient holds a valid insurance card                                     |
| Sepssis     | True   | Positive: if a patient in ICU will develop a sepsis , and Negative: otherwise |


# Structure
The directory contains app sub directories and a dataset for Sepsis :

1. [dev](https://github.com/kwasiasomani/Machine-Learning-FastAPI/tree/main/dev) folder model contains the model used for predicting , whether a person is suffering from sepsis or not, 6 hours before the onset. It also contains the files for all the pre- processing done. 
2. [src](https://github.com/kwasiasomani/Machine-Learning-FastAPI/tree/main/src) folder conains the fastapi app, requirements and the dockerfiles with its dependencies.


### How to run the project:

 Install the required packages to be able to run the evaluation locally.

You need to have [`Python 3`](https://www.python.org/) on your system (**a Python version lower than 3.10**). Then you can clone this repo and being at the repo's `https://github.com/kwasiasomani/Machine-Learning-FastAPI/tree/main`  follow the steps below:

- Windows:
        
        python -m venv venv; venv\Scripts\activate; python -m pip install -q --upgrade pip; python -m pip install -qr requirements.txt  

- Linux & MacOs:
        
        python3 -m venv venv; source venv/bin/activate; python -m pip install -q --upgrade pip; python -m pip install -qr requirements.txt  


### Dependencies

The following dependencies can be found in [requirements.txt](https://github.com/kwasiasomani/Machine-Learning-FastAPI/blob/main/src/requirements.txt):
1. [pandas](https://pandas.pydata.org/)
2. [Fastapi](https://fastapi.tiangolo.com/lo/)

### RandomForest along with other models is used to build the model. The model is tested on various other models. Details summary to be added soon.
### References

#### 1. Machine learning model:
![1](https://github.com/kwasiasomani/Machine-Learning-FastAPI/assets/119458164/13f01032-551e-4be6-89e8-f318e32b5586)

1. https://medium.com/themlblog/splitting-csv-into-train-and-test-data-1407a063dd74
2. https://towardsdatascience.com/multi-class-text-classification-model-comparison-and-selection-5eb066197568
3. https://medium.com/@robert.salgado/multiclass-text-classification-from-start-to-finish-f616a8642538
4. https://www.analyticsvidhya.com/blog/2018/04/a-comprehensive-guide-to-understand-and-implement-text-classification-in-python/
5. https://www.districtdatalabs.com/text-analytics-with-yellowbrick

#### 2. Fastapi building and deployment
 ## Screenshots
![1](https://github.com/kwasiasomani/Machine-Learning-FastAPI/assets/119458164/175a1c0a-063e-4cc4-9b23-d9c05bc86f78)
![2](https://github.com/kwasiasomani/Machine-Learning-FastAPI/assets/119458164/b3d9b1a6-7976-4e85-886d-3b91af9ccc9d)
![1](https://github.com/kwasiasomani/Machine-Learning-FastAPI/assets/119458164/dd4e04f4-0d1a-44d0-9e8c-82675444833f)

#The model can be view on huggingface
[Huggingface](https://huggingface.co/spaces/Kwasiasomani/Sepsis_Machine_Learning_API_using_FastAPI)




- [FastAPI for Machine Learning: Live coding an ML web application](https://www.youtube.com/watch?v=_BZGtifh_gw)
- [Video - Deploy ML models with FastAPI, Docker, and Heroku ](https://www.youtube.com/watch?v=h5wLuVDr0oc)
- [FastAPI Tutorial Series](https://www.youtube.com/watch?v=tKL6wEqbyNs&list=PLShTCj6cbon9gK9AbDSxZbas1F6b6C_Mx)
- [Http status codes](https://www.linkedin.com/feed/update/urn:li:activity:7017027658400063488?utm_source=share&utm_medium=member_desktop)

## Author

- [KWASI ASOMANI](https://www.linkedin.com/in/kwasi-asomani-61574920b/)
[![My Twitter Link](https://img.shields.io/twitter/follow/Asomani18?style=social)](https://twitter.com/Asomani18)
[Medium](https://medium.com/@kwasiasomani85/early-detection-of-sepsis-with-machine-learning-models-using-fastapi-3bfe41bc14e)
