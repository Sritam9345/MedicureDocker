from fastapi import FastAPI,APIRouter
from schema.main import UserModel
from model.main import predict
from db.db import collection_disease,collection_user 

router = APIRouter()


@router.post('/')
async def predict_disease(symtoms):
    print(type(symtoms))
    disease = await predict(symtoms)
    return disease

