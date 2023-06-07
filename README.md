# Machine-Learning-FastAPI On Sepsis 

The early prediction of sepsis is potentially life-saving, and we challenge participants to predict sepsis 6 hours before the clinical prediction of sepsis.
![image](https://github.com/kwasiasomani/Machine-Learning-FastAPI/assets/119458164/759c16c6-3e29-466b-9ce1-4ca96594d713)

# Abstract
Sepsis is a life-threatening condition with high mortality rates. Early detection and treatment are critical to improving outcomes

Sepsis occurs when chemicals released in the bloodstream to fight an infection trigger inflammation throughout the body. This can cause a cascade of changes that damage multiple organ systems, leading them to fail, sometimes even resulting in death.

# Structure
The directory contains app sub directories and a dataset for Sepsis :

1. [dev](https://github.com/kwasiasomani/Machine-Learning-FastAPI/tree/main/dev) folder model contains the model used for predicting , wether a person is suffering from sepsis or not, 6 hours before the onset. It also contains the files for all the pre- processing done. 
2. [src](https://github.com/kwasiasomani/Machine-Learning-FastAPI/tree/main/src) folder conains the fastapi app, requirements and the dockerfiles with its dependencies.


### How to run the project:

  1. Open the `Terminal`.
  2. Clone the repository by entering `https://github.com/kwasiasomani/Machine-Learning-FastAPI`.
  3. Ensure that `Python3` and `pip` are installed on the system.
  4. Create a `virtualenv` by executing the following command: `virtualenv venv`.
  6. Activate the `venv` virtual environment by executing the follwing command: `venv/Scripts/activate`.
  7. Enter the cloned repository directory and execute `pip install -r requirements.txt`.


### Dependencies

The following dependencies can be found in [requirements.txt](https://github.com/kwasiasomani/Machine-Learning-FastAPI/blob/main/src/requirements.txt):
1. [pandas](https://pandas.pydata.org/)
2. [Fastapi](https://fastapi.tiangolo.com/lo/)
