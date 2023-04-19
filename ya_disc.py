from imports import *

class YandexDisk:
    def __init__(self, token: str):
        self.token = token

# Загурзка на яндекс диск
    def upload(self, file_path: str, file_name):
        ya_path = f'/vk_backup/{file_name}'
        ya_upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = {'Content-Type': 'application/json',
                    'Authorization': f'OAuth {self.token}'}
        params = {"path": ya_path, "url": file_path}
        upload = requests.post(ya_upload_url, headers=headers, params=params)
        if upload.status_code == 202:
            return "upload comlete"
        else:
            return "error"