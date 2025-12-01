from sentence_transformers import SentenceTransformer, util
import pandas as pd
import numpy as np
import torch
import pickle 
from config.features import features

feature_embeddings = torch.load('nlp/tensor.pt')

with open('nlp/nlp.pkl','rb') as f:
    model = pickle.load(f)

print(feature_embeddings.shape)


class SymptomParser:
    
    def __init__(self):
        self.x_test = pd.DataFrame(np.zeros((1,132)),columns=features)

    def parser(self, symtoms):
        parts = symtoms.split(",")
        
        
        for sym in parts:
            enc = model.encode(sym, convert_to_tensor=True)
            cos_scores = util.pytorch_cos_sim(enc, feature_embeddings)[0]
            top_idx = int(torch.topk(cos_scores, k=1).indices[0])
            self.x_test.loc[0,features[top_idx]] = 1

        
