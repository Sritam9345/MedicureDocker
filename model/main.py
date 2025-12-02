import joblib
from nlp.main import SymptomParser
from encoder.encoder import Encoder


model = joblib.load("model/xgbc_v1.1.pkl")

parser = SymptomParser()
encoder = Encoder()
    
    
def predict(symptopms):
    parser.parser(symptopms)
    
    prediction = model.predict(parser.x_test)
    
    
    return encoder.encode_decode(prediction)
    
       
    