from functools import lru_cache
from pydantic import BaseSettings

class LocalConfigurations(BaseSettings):
    db: str
    db_username: str
    db_password: str
    db_host: str
    db_port: int
    db_name: str

    secret_key: str
    hash_algorithm: str
    access_token_expire_minutes: int
    
    class Config:
        env_file = "user_app/.env"
        secrets_dir = "user_app/.secrets"

@lru_cache()
def get_configurations():
    return LocalConfigurations()