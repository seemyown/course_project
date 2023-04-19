import requests
from pprint import pprint
import json
import time
from progress.bar import IncrementalBar
from tqdm import tqdm

# Создаем переменную с токеном ВКонтакте 
with open('vk_token.txt', 'r') as _vk:
    vk_token = _vk.read().strip()

# Создаем переменную с токеном Yandex 
with open('ya_token.txt', 'r') as ya:
    ya_token = ya.read().strip()