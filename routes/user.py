from fastapi import FastAPI,APIRouter
from schema.main import UserModel
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException
from model.main import predict
from schema.main import DiseaseModel
from db.db import collection_user, collection_disease

router = APIRouter()


@router.post('/create')
async def createUser(userData:UserModel):
    try:
        response  = collection_user.insert_one(dict(userData))
        return JSONResponse(status_code=200, content={"message":"User Created SucessFully"})
    except Exception as e:
        return HTTPException(status_code=500,detail=f"error occured{e}")
   


@router.get('/disease')
async def getDisease(userData):
    try:
        response = collection_disease.find({"user_id":userData._id})
        results = await response.to_list(length=None)
        return results
    except Exception as e:
        return HTTPException(status_code=500,detail=f"error occured{e}")


