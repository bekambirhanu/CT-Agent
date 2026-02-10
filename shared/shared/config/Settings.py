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

    # Windows VM Bridge (VirtualBox)
    MT5_BRIDGE_URL: str = os.getenv("MT5_BRIDGE_URL") or "http://localhost:8000"  # VirtualBox Host-Only IP
    MT5_PASSWORD: str
    MT5_LOGIN: int
    MT5_SERVER: str
    
    # App Config
    DEBUG: bool = False

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    def __str__(self):
        return super().__str__()
    
# Global instance
Settings = _Settings()


if __name__=='__main__':
    print(Settings)