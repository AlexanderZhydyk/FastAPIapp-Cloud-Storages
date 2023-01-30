from fastapi import FastAPI, File

from services import tasks

app = FastAPI(title="nimble_task")


@app.post("/upload")
def upload_data(filename: str, data: bytes = File()):
    answer = tasks.upload_data.delay(filename=filename, data=data)
    return answer.get()


@app.get("/download")
def download_data(filename: str):
    answer = tasks.download_data.delay(filename=filename)
    return answer.get()


if __name__ == '__main__':
    app()
