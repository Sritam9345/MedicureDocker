from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel , Field , computed_field
from schema.main import UserModel
from model.main import predict
from routes.user import userRouter
from routes.predict import PredictRouter


app = FastAPI()

    
@app.get("/")
def home():
    return {'message':"hi there"}

# @app.post("/predict")
# async def predict_disease(symtoms):
#     print(type(symtoms))
#     disease = await predict(symtoms)
#     type(disease)
#     return disease

app.include_router(PredictRouter,prefix='/predict')
app.include_router(userRouter,prefix='/user')

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)