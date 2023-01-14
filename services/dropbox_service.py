import dropbox

from typing import BinaryIO
from starlette import status
from starlette.responses import JSONResponse

from config import conf_dropbox
from services.abs_service import ApiMethods


class DropBoxMethods(ApiMethods):

    def __init__(self):
        self.client = self.get_credentials()

    @staticmethod
    def get_credentials():
        try:
            return dropbox.Dropbox(conf_dropbox.DROPBOX_ACCESS_TOKEN)
        except Exception as err:
            return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"message": err.message})

    def upload_file(self, file_name: str, data: BinaryIO):
        try:
            self.client.files_upload(data, file_name, mode=dropbox.files.WriteMode("overwright"))
            return JSONResponse(status_code=status.HTTP_200_OK, content={"message": True})
        except Exception as err:
            return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"message": err.message})

    def download_file(self, file_name):
        try:
            res = self.client.files_download(file_name)
            return JSONResponse(status_code=status.HTTP_200_OK, content={"message": str(res.content)})
        except Exception as err:
            return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"message": err.message})
