from pydantic import BaseModel , Field , computed_field
from enum import Enum


class Sex(str,Enum):
    
    M = "M"
    F = "F"


class UserModel(BaseModel):
    
    name: str
    age: int = Field(..., gt=18)
    sex: Sex
    height: float = Field(...,description="Enter in meters")
    weight: float = Field(...)
    
    
    @computed_field(return_type= float)
    def BMI(self):
        return float( self.weight/((self.height)*(self.height)) )


class DiseaseModel(BaseModel):
    
    user_id: str = "random"
    symptopms: str
    prognosis: str = "none"