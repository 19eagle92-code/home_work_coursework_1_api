import requests


class YandexDisk:
    def __init__(self, token):
        self.token = token
        self.headers = {"Authorization": f"OAuth {token}"}

    def create_folder(self, folder_name):
        """Создать папку на Яндекс.Диске"""
        response = requests.put(
            "https://cloud-api.yandex.net/v1/disk/resources",
            headers=self.headers,
            params={"path": folder_name}
        )
        
        if response.status_code == 201:
            print(f"Папка '{folder_name}' создана")
        elif response.status_code == 409:
            print(f"Папка '{folder_name}' уже существует")
        else:
            print("Ошибка создания папки")
        return response.status_code in [201, 409]

    def upload_from_url(self, folder_name, filename, image_url):
        """Загрузить файл по URL"""
        response = requests.post(
            "https://cloud-api.yandex.net/v1/disk/resources/upload",
            headers=self.headers,
            params={
                "path": f"{folder_name}/{filename}",
                "url": image_url
            }
        )
        return response.status_code == 202