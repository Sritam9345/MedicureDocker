import pickle
import joblib


model = joblib.load('encoder/labelencoder.pkl')

class Encoder():
    
    async def encode_decode(self,label: int):
        disease = model.inverse_transform([label])[0]
        return {"disease":disease}
        