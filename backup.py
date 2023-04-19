from ya_disc import *
from vk import *
from imports import *

# функция загрузки фото на диск
def backup(user, count = 5):
    vk_photo = VkUserPhoto(vk_token, '5.131')
    photos = vk_photo.getphoto(user, count)
    ya_upload = YandexDisk(ya_token)
    result = [] 
    bar = IncrementalBar("Загрузка на Я.Диск", max = count)
    if photos != 'error':
        try:
            print("Начало загрузки на Я.Диск")
            for photo in photos:
                upload = ya_upload.upload(photo['url'], photo['file_name'])
                if upload == "upload comlete":
                    result.append({'file_name':photo['file_name'],'size': photo['size']})

                bar.next()
                time.sleep(1)
            bar.finish()
            print("Фотографии загружены на Я.Диск")
            return result
        except:
            print("Ошибка загрузки на Я.Диск")


