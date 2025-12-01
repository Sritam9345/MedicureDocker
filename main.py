from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel , Field , computed_field
from schema.main import UserModel
from model.main import predict


app = FastAPI()

    
@app.get("/")
def home():
    return {'message':"hi there"}

@app.post("/predict")
async def predict_disease(symtoms):
    print(type(symtoms))
    disease = await predict(symtoms)
    return disease

    
    