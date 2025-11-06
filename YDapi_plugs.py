import requests


class YandexDiskApiPlugin:
    base_url = "https://cloud-api.yandex.net"

    def __init__(self, token):
        self.headers = {"Authorization": f"OAuth {token}"}

    def create_folder(self, folder_name):
        """Создание папки на яндекс диске"""
        params = {"path": folder_name}
        response = requests.put(
            f"{self.base_url}/v1/disk/resources", headers=self.headers, params=params
        )
        # словарь с вариантами ошибок
        status_codes = {
            201: f"📁 Папка '{folder_name}' успешно создана",
            409: f"📁 Папка '{folder_name}' уже существует",
            401: "⚠️ Ошибка авторизации: неверный токен",
            403: "⚠️ Недостаточно прав для создания папки",
            507: "⚠️ Недостаточно места на диске",
        }
        notice = status_codes.get(
            response.status_code, f" ⁉️ Неизвестная ошибка: {response.status_code}"
        )
        print(notice)
        return response.status_code == 201

    def upload_files(self, filename):
        """Загрузка файла на яндекс диск с компьютера"""
        params = {"path": f"dogs/{filename}"}
        response = requests.get(
            f"{self.base_url}/v1/disk/resources/upload",
            headers=self.headers,
            params=params,
        )
        if response.status_code != 200:
            raise Exception(f"Ошибка получения upload URL: {response.status_code}")

        upload_url = response.json()["href"]

        with open(f"{filename}", "rb") as f:
            upload_response = requests.put(upload_url, files={"file": f})
        return upload_response.status_code == 201

    def upload_from_url(self, folder_name, filename, image_url):
        """Загрузка файла на яндекс диск по URL"""
        params = {"path": f"{folder_name}/{filename}", "url": image_url}
        response = requests.post(
            f"{self.base_url}/v1/disk/resources/upload",
            headers=self.headers,
            params=params,
        )
        return response.status_code == 202

    def delete_folder(self, folder_name):
        """Удаление папки с яндекс диска"""
        params = {"path": folder_name}
        response = requests.delete(
            f"{self.base_url}/v1/disk/resources", headers=self.headers, params=params
        )
        return response.status_code == 204
