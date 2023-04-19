from imports import *

class VkUserPhoto:
    url = 'https://api.vk.com/method/'
    def __init__(self, token, version):
        self.params = {
            'access_token': token,
            'v': version    
        }
    # Получение фото пользователя
    def getphoto(self, owner_id, count):
        photos = []
        bar = IncrementalBar("Получение фотографий", max = count)
        getphoto_url = self.url + 'photos.get'
        getphoto_params = {
            'owner_id': owner_id,
            'album_id': 'profile', 
            'extended': '1',
            'count': count
        }

        try:
            items = requests.get(getphoto_url, params={**self.params, **getphoto_params}).json()['response']['items']
            for item in items:
                file_name = str(item['likes']['count'])+'_'+str(item['date'])+'.png'
                max_size = max(item['sizes'], key=lambda x: x['width'] * x['height'])
                photo_url = max_size['url']
                photos.append({"file_name": file_name, "url": photo_url, "size": max_size['type']})
                bar.next()
                time.sleep(1)
            bar.finish()
            print('Фотографии успешно получены')
            return photos
        except:
            print("Ошибка получения фотографий")
            return 'error'