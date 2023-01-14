from abc import ABC, abstractmethod


class ApiMethods(ABC):

    @abstractmethod
    def upload_file(self, file_name, data):
        pass

    @abstractmethod
    def download_file(self, file_name):
        pass
