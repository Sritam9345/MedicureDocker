from pydantic_settings import BaseSettings , SettingsConfigDict
from functools import lru_cache

class Setting(BaseSettings):
    
    mongo_url: str
    secret_key : str
    
    
    model_config = SettingsConfigDict(env_file='.env')


setting = Setting()