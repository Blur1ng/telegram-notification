from dotenv import load_dotenv
from pydantic_settings import BaseSettings
from pydantic import Field
load_dotenv()

class PostgreConSettings(BaseSettings):
    user:     str = Field("user",     env="user")
    password: str = Field("password", env="password")
    host:     str = Field("host",     env="host")
    port:     int = Field("port",     env="port")
    db:       str = Field("db",       env="db")

pg_settings = PostgreConSettings()