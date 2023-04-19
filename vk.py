from imports import *

class VkUserPhoto:
    url = 'https://api.vk.com/method/'
    def __init__(self, token, version):
        self.params = {
            'access_token': token,
            'v': version    
        }

    def getphoto(self, owner_id):
        photos = []
        getphoto_url = self.url + 'photos.get'
        getphoto_params = {
            'owner_id': owner_id,
            'album_id': 'profile', 
            # 'album_id': 'profile', 
            'extended': '1',
            # 'photo_sizes': '1',
            'count': '5'
        }
        print("Получение фотографий")
        try:
            items = requests.get(getphoto_url, params={**self.params, **getphoto_params}).json()['response']['items']
            for item in items:
                file_name = str(item['likes']['count'])+'.png'
                sizes = item['sizes']
                for size in sizes:
                    if size['type'] == 'w':
                        link = size['url']

                photos.append({"file_name": file_name, "url": link, "size": 'w'})
            print('Фотографии успешно получены')
        except:
            print("Ошибка получения фотографий")

        return photos