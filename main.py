import os
import sys
import requests
from tqdm import tqdm
import time
from dog_parser import Dogs
from YDapi_plugs import YandexDiskApiPlugin


def main():
    print("Скачиваем фото собок на ЯндексДиск ")

    # Токен
    token = input("Введите ВАШ токен ЯндексДиска")

    # Ввод породы
    breed = input("Введите породу собаки(на английском): ")

    # Получаем фото
    dogs = Dogs()
    dogs.get_one_image_per_subbreed(breed)

    if not dogs.images:
        print("Не найдено изображений для загрузки")
        return

    # Яндекс.Диск
    yandex = YandexDiskApiPlugin(token)
    folder_name = f"dogs_{breed}"

    if not yandex.create_folder(folder_name):
        return

    # Загружаем с tqdm
    print(f"\nЗагрузка на Яндекс.Диск:")

    successful = 0
    for image in tqdm(dogs.images, desc="Загрузка", unit="файл"):
        if yandex.upload_from_url(folder_name, image["filename"], image["url"]):
            successful += 1
        time.sleep(0.1)

    # Сохраняем информацию
    dogs.save_json()

    # Итог
    print(f"Готово!")
    print(f"✅ Успешно загружено: {successful}/{len(dogs.images)}")


if __name__ == "__main__":
    main()
