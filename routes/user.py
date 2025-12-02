from fastapi import FastAPI,APIRouter ,Request
from schema.main import UserModel
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException
from config.config import setting
from bson import ObjectId
from db.db import collection_user, collection_disease
import jwt


userRouter = APIRouter()

@userRouter.post('/create')
async def createUser(userData:UserModel):
    print(setting.secret_key)
    try:
        response  = collection_user.insert_one(dict(userData))
        userId = str(response.inserted_id)
        token = jwt.encode({"user_id":userId},setting.secret_key,algorithm="HS256")
        return JSONResponse(status_code=200, content={"message":"User Created SucessFully" , "token":str(token)})
    except Exception as e:
        return HTTPException(status_code=500,detail=f"error occured{e}")



@userRouter.get('/disease')
async def getDisease(request: Request):
    
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
        return JSONResponse(status_code=401, content={"detail": "Invalid Token"})
   
    user_id = getattr(request.state, "user_id", None)
    
    try:
       
        response = collection_disease.find({"user_id":user_id})
        results = []
        for docs in response:
            docs['_id'] = str(docs['_id'])
            docs['user_id'] = str(docs['user_id'])
            results.append(docs)
        return results
    except Exception as e:
        return HTTPException(status_code=500,detail=f"error occured{e}")


