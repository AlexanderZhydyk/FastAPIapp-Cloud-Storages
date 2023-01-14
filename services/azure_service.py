from azure.storage.blob import BlobServiceClient
from typing import BinaryIO
from starlette import status
from starlette.responses import JSONResponse

from config import conf_azure
from services.abs_service import ApiMethods


class AzureService(ApiMethods):

    def __init__(self):
        self.container = "nimbletask"
        self.client = self.get_credentials()

    def _get_blob_client(self, container: str, filename: str):
        return self.client.get_blob_client(container=container, blob=filename)

    @staticmethod
    def get_credentials():
        return BlobServiceClient.from_connection_string(conf_azure.AZURE_CONNECTION_STRING)

    def upload_file(self, filename: str, data: BinaryIO):
        try:
            blob_client = self._get_blob_client(self.container, filename)
            blob_client.upload_blob(data)
            return JSONResponse(status_code=status.HTTP_200_OK, content={"message": True})
        except Exception as err:
            print(err)
            return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"message": err.message})

    def download_file(self, filename: str):
        try:
            blob_client = self._get_blob_client(self.container, filename)
            data = blob_client.download_blob().readall()  # chunks()
            return JSONResponse(status_code=status.HTTP_200_OK, content={"message": str(data)})
        except Exception as err:
            return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"message": err.message})
