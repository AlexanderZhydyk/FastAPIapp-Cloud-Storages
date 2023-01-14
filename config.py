from pydantic import BaseSettings, Field


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
