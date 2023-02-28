from fastapi import FastAPI, UploadFile, File, Depends

from services import tasks
from services.azure_service import AzureService


app = FastAPI(title="nimble_task")

def get_service():
    return AzureService()


@app.post("/upload")
def upload_data(filename: str, data: bytes = File(), service: AzureService = Depends(get_service)):
    return tasks.upload_data.delay(filename=filename, data=data, service=service).get()


@app.get("/download")
def download_data(filename: str, service: AzureService = Depends(get_service)):
    response = tasks.download_data.delay(filename=filename, service=service)
    return response.get()


@app.get("/list")
def get_files_list(service: AzureService = Depends(get_service)):
    return tasks.get_files_list.delay(service).get()


@app.delete("/delete")
def delete_file(filename: str, service: AzureService = Depends(get_service)):
    return tasks.delete_file.delay(filename=filename, service=service).get()


if __name__ == '__main__':
    app()
