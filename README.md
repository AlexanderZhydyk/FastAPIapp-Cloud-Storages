# FastAPI Cloud Storages

The FastAPI Cloud Storages module supports Azure, Dropbox cloud storage providers. Supports  upload, download, delete and list of stored files.

## Prerequisites

At first, you should create app in Cloud Providers:

[Azure Blob Storage Quickstart](https://learn.microsoft.com/en-us/azure/storage/blobs/storage-quickstart-blobs-python)

[Dropbox Python Guide](https://www.dropbox.com/developers/reference/getting-started?_tk=guides_lp&_ad=tutorial5&_camp=get_started#app%20console)


## Installing

1. Clone the repo:
```sh
git clone https://github.com/AlexandrZhydyk/FastAPIapp-Cloud-Storages.git
```
2. Install dependencies:
```shell
pipenv install
```
3. Install redis server on your host machine:
```shell
sudo apt-get install redis-server
```
4. Add environment variables to ``config.py``:

* `DROPBOX_ACCESS_TOKEN`: `REQUIRED`
* `AZURE_CONNECTING_STRING`: `REQUIRED`
* `REDIS_HOST`: `REQUIRED`
* `REDIS_PORT`: `REQUIRED`
* `REDIS_DB`: `REQUIRED`

## Usage

Run application:
```python
uvicorn app:app --reload
```
Run celery:
```shell
celery -A services.tasks.celery_app worker -l info --pool=prefork
```

## TODO
- [x] Add celery
- [ ] Implement caching support for large files
- [ ] Add tests
- [ ] Add delete, get list features for Dropbox service



