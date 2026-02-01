import os
from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional

load_dotenv(dotenv_path=f"{os.curdir}/../../.env")



class _Settings(BaseSettings):
    """
    Settings for environment variables and constant configurations
    """
    
    # model config
    
    MODEL_API_KEY: str = os.getenv("MODEL_API_KEY") | None
    MODEL_NAME: str = os.getenv("MODEL_NAME") | None
    MODEL_BASE_URL: str =os.getenv("MODEL_BASE_URL") | None
    
    # Telegram Config
    TELEGRAM_BOT_TOKEN: str

    # Broker Config (Exness/MT5)
    MT5_LOGIN: Optional[int] = None
    MT5_PASSWORD: Optional[str] = None
    MT5_SERVER: Optional[str] = None

    # App Config
    DEBUG: bool = False

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


# Global instance
Settings = _Settings()


if __name__=='__main__':
    print(Settings)