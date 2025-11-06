import requests
import json
import sys


class Dogs:
    base_url = "https://dog.ceo/api"

    def __init__(self):
        # self.images = []
        self.image_url = None
        # self.filename = None

    def get_one_image_per_subbreed(self, breed):
        """Получить по одному изображению для каждой под-породы"""
        self.images = []

        print(f"Проверяем под-породы для '{breed}'...")

        # Проверяем есть ли под-породы
        subbreeds_response = requests.get(f"{self.base_url}/breed/{breed}/list")

        if subbreeds_response.json()["status"] != "success":
            print("Такая порода не найдена")
            return

        subbreeds = subbreeds_response.json()["message"]

        if subbreeds:
            # ЕСТЬ под-породы - загружаем по одному изображению для каждой
            print(f"Найдены под-породы: {', '.join(subbreeds)}")
            for subbreed in subbreeds:
                self._download_one_subbreed_image(breed, subbreed)
        else:
            # НЕТ под-пород - загружаем одно изображение основной породы
            print(f"Под-породы не найдены, загружаем основную породу...")
            self._download_one_breed_image(breed)

    def _download_one_breed_image(self, breed):
        """Загрузить одно случайное изображение основной породы"""
        response = requests.get(f"{self.base_url}/breed/{breed}/images/random")

        if response.json()["status"] == "success":
            image_url = response.json()["message"]
            filename = image_url.split("/")[-1]
            self.images.append(
                {
                    "breed": breed,
                    "subbreed": None,
                    "url": image_url,
                    "filename": f"{breed}_{filename}",
                }
            )
            print(f"✅ Загружено 1 фото основной породы {breed}")

    def _download_one_subbreed_image(self, breed, subbreed):
        """Загрузить одно случайное изображение под-породы"""
        response = requests.get(
            f"{self.base_url}/breed/{breed}/{subbreed}/images/random"
        )

        if response.json()["status"] == "success":
            image_url = response.json()["message"]
            filename = image_url.split("/")[-1]
            self.images.append(
                {
                    "breed": breed,
                    "subbreed": subbreed,
                    "url": image_url,
                    "filename": f"{breed}_{subbreed}_{filename}",
                }
            )
            print(f"✅ Загружено 1 фото для под-породы {subbreed}")

    def get_random_picture(self):
        """Получить случайное изображение собаки"""
        response = requests.get(f"{self.base_url}/breed/{self.breed}/images/random")
        if response.json()["status"] != "success":
            print("Такая порода не найдена")
            sys.exit(0)
        self.image_url = response.json()["message"]
        self.filename = self.image_url.split("/")[-1]
        return True

    def get_breed_images(self, breed):
        """Получить все изображения породы и под-пород"""
        self.images = []

        print(f" Проверяем под-породы для '{breed}'...")

        # 1. Сначала проверяем есть ли под-породы
        subbreeds_response = requests.get(f"{self.base_url}/breed/{breed}/list")

        if subbreeds_response.json()["status"] != "success":
            print("Такая порода не найдена")
            return

        subbreeds = subbreeds_response.json()["message"]

        if subbreeds:
            # ЕСТЬ под-породы - загружаем каждую
            print(f" Найдены под-породы: {', '.join(subbreeds)}")
            for subbreed in subbreeds:
                self._download_subbreed_images(breed, subbreed)
        else:
            # НЕТ под-пород - загружаем основную породу
            print(f"📷 Загружаем основную породу {breed}...")
            self._download_breed_images(breed)

    def _download_breed_images(self, breed):
        """Загрузить изображения основной породы (без под-пород)"""
        response = requests.get(f"{self.base_url}/breed/{breed}/images")

        if response.json()["status"] == "success":
            images = response.json()["message"]
            for image_url in images:
                filename = image_url.split("/")[-1]
                self.images.append(
                    {
                        "breed": breed,
                        "subbreed": None,  # ОСНОВНАЯ порода - subbreed = null
                        "url": image_url,
                        "filename": f"{breed}_{filename}",
                    }
                )
            print(f"✅ Загружено {len(images)} фото основной породы")

    def _download_subbreed_images(self, breed, subbreed):
        """Загрузить изображения под-породы"""
        response = requests.get(f"{self.base_url}/breed/{breed}/{subbreed}/images")

        if response.json()["status"] == "success":
            images = response.json()["message"]
            for image_url in images:
                filename = image_url.split("/")[-1]
                self.images.append(
                    {
                        "breed": breed,
                        "subbreed": subbreed,  # ПОД-ПОРОДА - subbreed = название
                        "url": image_url,
                        "filename": f"{breed}_{subbreed}_{filename}",
                    }
                )
            print(f"✅ Загружено {len(images)} фото для {subbreed}")

    def save_json(self, filename="dogs_info.json"):
        """Сохранить информацию в JSON"""
        with open(filename, "w") as f:
            json.dump(self.images, f, indent=2)
        print(f"Информация о породе сохранена в {filename}")
