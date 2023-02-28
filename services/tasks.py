from celery import Celery
from fastapi.params import Depends

from config import conf_redis
from services.azure_service import AzureService

celery_app = Celery(
    "tasks",
    broker=f'redis://{conf_redis.REDIS_HOST}:{conf_redis.REDIS_PORT}/{conf_redis.REDIS_DB}',
    backend=f'redis://{conf_redis.REDIS_HOST}:{conf_redis.REDIS_PORT}/{conf_redis.REDIS_DB}',
)

celery_app.conf.event_serializer = 'pickle'
celery_app.conf.task_serializer = 'pickle'
celery_app.conf.result_serializer = 'pickle'
celery_app.conf.accept_content = ['application/json', 'application/x-python-serialize']


@celery_app.task(default_retry_delay=300, max_retries=3)
def upload_data(filename: str, data: bytes, service: AzureService):
    return service.upload_file(filename, data)


@celery_app.task(default_retry_delay=300, max_retries=3)
def download_data(filename: str, service: AzureService):
    return service.download_file(filename)


@celery_app.task(default_retry_delay=300, max_retries=3)
def get_files_list(service: AzureService):
    return service.get_files_list()


@celery_app.task(default_retry_delay=300, max_retries=3)
def delete_file(filename: str, service: AzureService):
    return service.delete_file(filename)

