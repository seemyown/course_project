from imports import *

class YandexDisk:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str, file_name):
        ya_path = f'/vk_backup/{file_name}'
        ya_upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = {'Content-Type': 'application/json',
                    'Authorization': f'OAuth {self.token}'}
        # params = {"path": ya_path, "overwrite": "true"}
        params = {"path": ya_path, "url": file_path}
        # response = requests.get(ya_upload_url, headers=headers, params=params)

        # print(response.json()["href"])
        # upload = requests.put(response.json()["href"], file_path)\
        upload = requests.post(ya_upload_url, headers=headers, params=params)
        # print(upload.status_code)
        if upload.status_code == 202:
            # print("Фотографии загружены на диск")
            return "upload comlete"
        else:
            # print("Ошибка загрузки на диск")
            return "error"