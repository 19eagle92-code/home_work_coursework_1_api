import os
import sys
import requests
from tqdm import tqdm
import time
from dog_parser import Dogs
from YDapi_plugs import YandexDiskApiPlugin
import random


def main():
    print("Скачиваем фото собок на ЯндексДиск ")

    # Токен
    token = input("Введите ВАШ токен ЯндексДиска")

    # Ввод породы
    breed = input("Введите породу собаки(на английском): ")

    # Получаем фото
    dogs = Dogs()
    dogs.get_breed_images(breed)

    print(f"Всего фото: {len(dogs.images)}")

    count_img = int(input("сколько фотографий хотите сохранить"))

    # Выбираем случайные фотографии по количеству
    if len(dogs.images) > count_img:
        images = random.sample(dogs.images, count_img)
    else:
        images = dogs.images

    print(f"Загружаем СЛУЧАЙНЫЕ {len(images)} фото")

    # Яндекс.Диск
    yandex = YandexDiskApiPlugin(token)
    folder_name = f"dogs_{breed}"

    if not yandex.create_folder(folder_name):
        return

    # Загружаем с tqdm
    print(f"\nЗагрузка на Яндекс.Диск:")

    successful = 0
    for image in tqdm(images, desc="Загрузка", unit="файл"):
        if yandex.upload_from_url(folder_name, image["filename"], image["url"]):
            successful += 1
        time.sleep(0.1)

    # Сохраняем инфо
    dogs.save_json()

    # Итоги
    print(f"Готово!")
    print(f"✅ Успешно: {successful}/{len(images)}")


if __name__ == "__main__":
    main()
