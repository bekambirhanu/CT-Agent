import os
from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional

# Load .env from project root
project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
load_dotenv(dotenv_path=os.path.join(project_root, ".env"))



class _Settings(BaseSettings):
    """
    Settings for environment variables and constant configurations
    """
    
    # model config
    
    MODEL_API_KEY: str = os.getenv("MODEL_API_KEY") or ""
    MODEL_NAME: str = os.getenv("MODEL_NAME") or ""
    MODEL_BASE_URL: str = os.getenv("MODEL_BASE_URL") or ""
    
    # Telegram Config
    TELEGRAM_BOT_TOKEN: str = os.getenv("TELEGRAM_BOT_TOKEN") or ""

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