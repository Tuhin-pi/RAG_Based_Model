import os
# from pydantic_settings import BaseSettings
# from typing import Optional

class Settings():
    def __init__(self):
        # API Configuration
        self.API_V1_STR: str = "/api/v1"
        self.PROJECT_NAME: str = "YouTube ChatBot"
        self.VERSION: str = "1.0.0"

        # Server Configuration
        self.HOST: str = "0.0.0.0"
        self.PORT: int = 8000
        self.DEBUG: bool = False

        self.MONGODB_URL: str = os.getenv("MONGODB_URL")
        self.DATABASE_NAME: str = os.getenv("DATABASE_NAME", "youtube_chatbot")
        self.VECTOR_COLLECTION: str = "transcript_embeddings"
        self.CHAT_COLLECTION: str = "chat_history"

        # Vector Store Configuration
        self.VECTOR_DIMENSION: int = 1536
        self.CHUNK_SIZE: int = 1000
        self.CHUNK_OVERLAP: int = 200
        self.CHUNK_SEPARATORS:list = [""]

        # Retrieval Configuration
        self.RETRIEVAL_K: int = 5
        self.SIMILARITY_THRESHOLD: float = 0.7
        
        # Rate Limiting
        self.RATE_LIMIT_REQUESTS: int = 100
        self.RATE_LIMIT_WINDOW: int = 3600  # 1 hour

        # class Config:
        #     env_file = ".env"
        #     case_sensitive = True

settings = Settings()