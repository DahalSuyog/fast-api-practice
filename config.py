from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "sqlite:///./metadata.db"
    QDRANT_HOST: str = "localhost"
    QDRANT_PORT: int = 6333
    COLLECTION_NAME: str = "documents"
    EMBEDDING_MODEL: str = "all-MiniLM-L6-v2"  # Free local model

    class Config:
        env_file = ".env"

settings = Settings()