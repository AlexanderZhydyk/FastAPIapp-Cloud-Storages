from fastapi import FastAPI, UploadFile, File

from services import tasks

app = FastAPI(title="nimble_task")


@app.post("/upload")
def upload_data(filename: str, data: bytes = File()):
    return tasks.upload_data.delay(filename=filename, data=data).get()


@app.get("/download")
def download_data(filename: str):
    return tasks.download_data.delay(filename=filename).get()


@app.get("/list")
def get_files_list():
    return tasks.get_files_list.delay().get()


@app.delete("/delete")
def delete_file(filename: str):
    return tasks.delete_file.delay(filename=filename).get()


if __name__ == '__main__':
    app()
