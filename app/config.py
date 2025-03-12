
import os

from dotenv import load_dotenv



# Configuration class
class Config:
    
    api_url: str = os.getenv("API_URL")
    api_key: str = os.getenv("API_KEY")
    
    headers: dict = {
        
        "x-api-key": api_url,
        "Content-Type": "application/json"
    }
    