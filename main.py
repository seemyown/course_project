from backup import *


vk_id = input('Введите id Вконтакте:') #Official

# Запись информации в файл
response = {}
response["response"] = backup(vk_id)

with open('result.json', 'w') as file:
    json.dump(response, file, ensure_ascii=False, indent=4)
