from ya_disc import *
from vk import *
from imports import *

# Создаем переменную с токеном ВКонтакте 
with open('vk_token.txt', 'r') as _vk:
    vk_token = _vk.read().strip()

# Создаем переменную с токеном Yandex 
with open('ya_token.txt', 'r') as ya:
    ya_token = ya.read().strip()



# vk_id = input('Введите id Вконтакте: ') #Official
vk_id = '400314360' # Test
# vk_id = '1'
# print(vk_photo.getphoto(vk_id))

# vk_photo = VkUserPhoto(vk_token, '5.131')
# data = vk_photo.getphoto(vk_id)
# pprint(vk_photo.getphoto(vk_id))



def backup(user):
    vk_photo = VkUserPhoto(vk_token, '5.131')
    photos = vk_photo.getphoto(user)
    ya_upload = YandexDisk(ya_token)
    result = [] 
    try:
        print("Начало загрузки на Я.Диск")
        for photo in photos:
            upload = ya_upload.upload(photo['url'], photo['file_name'])
            if upload == "upload comlete":
                print(f"Фотография {photo['file_name']} загружена на Я.Диск")
                result.append({'file_name':photo['file_name'],'size': photo['size']})
        print("Фотографии загружены на Я.Диск")
        return result
    except:
        print("Ошибка загрузки на Я.Диск")


# backup(vk_id)


response = {}
response["response"] = backup(vk_id)

with open('result.json', 'w') as file:
    json.dump(response, file)
