import requests
import sys


class Dogs:
    base_url = "https://dog.ceo/api"

    def __init__(self, breed):
        self.breed = breed
        self.image_url = None
        self.filename = None

    def get_random_picture(self):
        """Получить случайное изображение собаки"""
        response = requests.get(f"{self.base_url}/breed/{self.breed}/images/random")
        if response.json()["status"] != "success":
            print("Такая порода не найдена")
            sys.exit(0)
        self.image_url = response.json()["message"]
        self.filename = self.image_url.split("/")[-1]
        return True

    def save_pic(self):
        """Сохранить изображение на компьютер"""
        if not self.image_url:
            self.get_random_picture()

        response = requests.get(self.image_url)
        with open(f"{self.filename}", "wb") as f:
            f.write(response.content)
        print(f"Изображение сохранено как: {self.filename}")
