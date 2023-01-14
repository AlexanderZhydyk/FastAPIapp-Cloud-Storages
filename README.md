# FastAPI Cloud Storages

The FastAPI Cloud Storages module supports Azure, Dropbox cloud storage providers. Supports upload, download stored files.


## Prerequisites

At first, you should create app in Cloud Providers:

[Azure Blob Storage Quickstart](https://learn.microsoft.com/en-us/azure/storage/blobs/storage-quickstart-blobs-python)

[Dropbox Python Guide](https://www.dropbox.com/developers/reference/getting-started?_tk=guides_lp&_ad=tutorial5&_camp=get_started#app%20console)


## Installing

1. Clone the repo:
```sh
git clone https://github.com/AlexandrZhydyk/PartsOnlineStore.git
```
2. Install dependencies:
```shell
pipenv install
```
3. Add environment variables to ``config.py``:

* `DROPBOX_ACCESS_TOKEN`: `REQUIRED`
* `AZURE_CONNECTING_STRING`: `REQUIRED`

## Usage

Run application:
```python
uvicorn app:app --reload
```





