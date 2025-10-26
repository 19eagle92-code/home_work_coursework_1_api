import os
import sys
import requests
from tqdm import tqdm
import time
from dog_parser import Dogs
from YDapi_plugs import YandexDiskApiPlugin

# from fff import YandexDiskApiPlugin


# if __name__ == "__main__":
#     # Запрашиваем породу и токен у пользователя
#     breed = input("Введите породу собаки на английском: ")
#     # token = input(str("введите(вставьте) ваш токен:"))
#     token = "y0__xCqldXFBBjblgMg2LyK8xQwmaadnQgCBWderre4Qwhn1CRw7zGWciFW8Q"

#     # Создаем объект класса Dogs
#     dog = Dogs(breed)
#     yd = YandexDiskApiPlugin(token)

#     # Получаем и сохраняем изображение
#     dog.get_random_picture()
#     dog.save_pic()
#     yd.create_folder()
#     yd.upload_files()


def main():
    # Получаем породу собаки
    # breed = input("Введите породу собаки: ")
    breed = "corgi"
    # Ищем изображение собаки
    dog = Dogs(breed)
    dog.get_random_picture()
    print(f"Найдено изображение: {dog.filename}")

    # Скачиваем изображение
    # dog.save_pic()

    # Загружаем на Яндекс.Диск
    # token = input("Введите токен Яндекс.Диска: ")
    token = "y0__xCqldXFBBjblgMg2LyK8xQwmaadnQgCBWderre4Qwhn1CRw7zGWciFW8Q"
    yandex = YandexDiskApiPlugin(token)

    # Создаем папку и загружаем
    yandex.create_folder("dogs")
    yandex.url_upload("dogs", dog.filename, dog.image_url)
    # if yandex.upload_files(dog.filename):
    #     print(f"✅ Изображение {dog.filename} загружено на Яндекс.Диск")


if __name__ == "__main__":
    main()
