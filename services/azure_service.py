from azure.storage.blob import BlobServiceClient
from starlette import status
from starlette.responses import JSONResponse

from config import conf_azure


class AzureService:

    def __init__(self):
        self.container = "nimbletask"
        self.client = self.get_credentials()

    def _get_blob_client(self, container: str, filename: str):
        return self.client.get_blob_client(container=container, blob=filename)

    @staticmethod
    def get_credentials():
        return BlobServiceClient.from_connection_string(conf_azure.AZURE_CONNECTION_STRING)

    def upload_file(self, filename: str, data: bytes):
        try:
            blob_client = self._get_blob_client(self.container, filename)
            if not blob_client.exists():
                blob_client.upload_blob(data)
                return JSONResponse(status_code=status.HTTP_200_OK, content={"message": "Blob uploaded successfully!"})
            return JSONResponse(status_code=status.HTTP_200_OK, content={"message": "Blob already exists!"})
        except Exception as err:
            print("Failed to upload files to container. Error:" + str(err))

    def download_file(self, filename: str):
        try:
            blob_client = self._get_blob_client(self.container, filename)
            if blob_client.exists():
                data = blob_client.download_blob().readall()  # chunks()
                return JSONResponse(status_code=status.HTTP_200_OK, content={"message": str(data)})
            return JSONResponse(status_code=status.HTTP_200_OK, content={"message": f"there is no file named {filename}"})
        except Exception as err:
            print("Failed to delete blob. Error:" + str(err))

    def get_files_list(self):
        try:
            blobs_list_response = self.client.get_container_client(self.container).list_blobs()
            blob_lst = []
            for r in blobs_list_response:
                blob_lst.append(r.name)
            return blob_lst
        except Exception as err:
            print("Failed to get the blob list in the container. Error:" + str(err))

    def delete_file(self, filename: str):
        try:
            blob_client = self._get_blob_client(self.container, filename)
            if blob_client.exists():
                blob_client.delete_blob()
                return JSONResponse(status_code=status.HTTP_200_OK, content={"message": "Blob deleted successfully!"})
            else:
                return JSONResponse(status_code=status.HTTP_200_OK, content={"Blob does not exist!"})
        except Exception as err:
            print("Failed to delete blob. Error:" + str(err))

    def __str__(self):
        return 'azure_service'
