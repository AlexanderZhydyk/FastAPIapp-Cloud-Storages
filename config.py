from pydantic import BaseSettings, Field


class RedisConfig(BaseSettings):
    REDIS_HOST: str = Field(..., env='REDIS_HOST')
    REDIS_PORT: int = Field(..., env='REDIS_PORT')
    REDIS_DB: str = Field(..., env='REDIS_DB')

    class Config:
        case_sensitive = True
        env_file = '.env'
        env_file_encoding = 'utf-8'


class AzureBlobConfig(BaseSettings):
    AZURE_CONNECTION_STRING: str = Field(..., env='AZURE_CONNECTION_STRING')

    class Config:
        case_sensitive = True
        env_file = '.env'
        env_file_encoding = 'utf-8'


class DropBoxConfig(BaseSettings):

    DROPBOX_ACCESS_TOKEN: str = Field(..., env='DROPBOX_ACCESS_TOKEN')

    class Config:
        case_sensitive = True
        env_file = '.env'
        env_file_encoding = 'utf-8'


conf_azure = AzureBlobConfig()
conf_dropbox = DropBoxConfig()
conf_redis = RedisConfig()
