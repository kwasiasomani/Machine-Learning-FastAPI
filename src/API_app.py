"""
FastAPI script for Sepsis and model prediction
Author: Equity
Date: May.30th 2023
"""


# The library for the API Code
from fastapi import FastAPI
import pickle
import uvicorn
from pydantic import BaseModel
import pandas as pd



# Declare the data with its components and their type
class model_input(BaseModel):
    
    PRG: int
    PL: int
    PR: int
    SK: int
    TS: int
    M11: float
    BD2: float
    Age: int
    Insurance:int


app = FastAPI(title = 'Sepsis API',
              description = 'An API that takes input and display the predictions',
              version = '0.1.0')

# Load the saved data
toolkit = "app\Scaler &ML toolkit"

def load_toolkit(filepath = toolkit):
    with open(toolkit, "rb") as file:
        loaded_toolkit = pickle.load(file)
    return loaded_toolkit

toolkit = load_toolkit()
scaler = toolkit["scaler"]
model = toolkit["model"]


@app.get("/")
async def hello():
    return "Welcome to our model API"



@app.post("/Sepssis")
async def prediction(input:model_input):
   data = {
           'PRG': input.PRG, 
           'PL': input.PL,
           'PR': input.PR,
           'SK': input.SK,
           'TS': input.TS,
           'M11': input.M11,
           'BD2': input.BD2,
           'Age': input.Age,
           'Insurance': input.Insurance,
                }
   
# prepare the data as a dataframe
   df = pd.DataFrame(data, index=[0])


   #numerical features
   numeric_columns =  [ 'PRG', 'PL', 'PR', 'SK', 'TS', 'M11', 'BD2', 'Age','Insurance']
   
   #scaling
   Scaler = scaler.transform(df[numeric_columns])
   Scaled = pd.DataFrame(Scaler)                  
   prediction = model.predict(Scaled).tolist()
   probability = model.predict_proba(Scaled)


    # Labelling Model output
   if (prediction[0] < 0.5):
         prediction = "Negative. This person has no Sepssis"
   else: 
      prediction = "Positive. This person has Sepssis"
   data['prediction'] = prediction  
   return data
   
   
        


# Launch the app
if __name__ == "__main__":
 uvicorn.run("API_app:app",host = '127.0.0.1', port = 8091)