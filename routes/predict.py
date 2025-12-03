from fastapi import FastAPI, APIRouter, Request
from schema.main import DiseaseModel
from model.main import predict
import jwt
from fastapi.responses import JSONResponse
from config.config import setting
from bson import ObjectId
from db.db import collection_disease, collection_user  

app = FastAPI()
PredictRouter = APIRouter()

@PredictRouter.post("/")
async def predict_disease(symptoms: DiseaseModel, request: Request):
    
    auth_header = request.headers.get("Authorization")
    if not auth_header or not auth_header.startswith("Bearer "):
        return JSONResponse(status_code=401, content={"detail": "Missing or invalid token"})

    token = auth_header.split(' ')[1]
    token = token.strip()
    try:
        
        payload = jwt.decode(token, setting.secret_key,algorithms="HS256")
        user_id = payload.get("user_id")
        print(token)
        if not user_id:
            return JSONResponse(status_code=401, content={"detail": "Invalid token payload"})
        request.state.user_id = ObjectId(user_id)
    except Exception as e:
        return JSONResponse(status_code=401, content={"detail": f"Invalid{e}"})
   
    symptoms.user_id = getattr(request.state, "user_id", None)
    disease = await predict(symptoms.symptopms)

    symptoms.prognosis = disease
    try:
        collection_disease.insert_one(dict(symptoms))
        symptoms.user_id = str(symptoms.user_id)
        return dict(symptoms)
    except Exception as e:
        return JSONResponse(status_code=500, content={"message": f"{e}"})

