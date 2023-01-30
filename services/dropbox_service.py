import dropbox

from typing import BinaryIO

from celery import shared_task
from starlette import status
from starlette.responses import JSONResponse

from config import conf_dropbox
from services.abs_service import ApiMethods


class DropboxService(ApiMethods):

    def __init__(self):
        self.client = self.get_credentials()

    @staticmethod
    def get_credentials():
        try:
            return dropbox.Dropbox(conf_dropbox.DROPBOX_ACCESS_TOKEN)
        except Exception as err:
            return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"message": err.message})

    # @shared_task
    def upload_file(self, file_name: str, data: bytes):
        try:
            self.client.files_upload(data, file_name, mode=dropbox.files.WriteMode.overwrite)
            return JSONResponse(status_code=status.HTTP_200_OK, content={"message": True})
        except Exception as err:
            return str(err)
            # return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"message": err.message})

    # @shared_task
    def download_file(self, file_name):
        try:
            res = self.client.files_download(file_name)
            return JSONResponse(status_code=status.HTTP_200_OK, content={"message": str(res.content)})
        except Exception as err:
            return err
            # return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"message": err})

    def __str__(self):
        return 'dropbox_service'
