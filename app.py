from fastapi import FastAPI, Depends, File

from services.azure_service import AzureService

app = FastAPI(title="nimble_task")


def get_service():
    return AzureService()


@app.post("/upload")
def upload_data(file_name: str, data: bytes = File(), service=Depends(get_service)):
    return service.upload_file(file_name, data)


@app.get("/download")
def download_data(file_name: str, service=Depends(get_service)):
    return service.download_file(file_name)


if __name__ == '__main__':
    app()
