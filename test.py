import time
from tqdm import tqdm


def main():
    print("✅ Виртуальная среда работает!")
    print("✅ Проект настроен в VS Code!")

    # Проверим что мы в виртуальной среде
    import sys

    print(f"✅ Python путь: {sys.prefix}")

    # Проверим установленные пакеты
    try:
        import requests
        from tqdm import tqdm

        print(f"✅ Requests установлен: {requests.__version__}")
        print(f"✅ tqdm установлен: {tqdm}")
    except ImportError:
        print("❌ Requests не установлен")


if __name__ == "__main__":
    main()


for i in tqdm(range(100)):
    time.sleep(0.01)


# 1) спросить пользователя породу собаки и получить информацию о картинке с этой породой
breed = input("Введите название породы (на английском): ")
url = f"https://dog.ceo/api/breed/{breed}/images/random"
response = requests.get(url)
if response.json()["status"] != "success":
    print("Такая порода не найдена")
    sys.exit(0)
image_url = response.json()["message"]
filename = image_url.split("/")[-1]

# 2) скачать эту картинку на компьютер
response = requests.get(image_url)
with open(f"{filename}", "wb") as f:
    f.write(response.content)


# 3) создать на яндекс-диске папку для хранения картинок
yd_url = "https://cloud-api.yandex.net/v1/disk/resources"
params = {"path": "dogs"}
token = input(str("введите(вставьте) ваш токен:"))
headers = {"Authorization": f"OAuth {token}"}
response = requests.put(yd_url, params=params, headers=headers)

# 4) загрузить картинку с компьютера в эту папку
params = {"path": f"dogs/{filename}"}
response = requests.get(
    "https://cloud-api.yandex.net/v1/disk/resources/upload",
    headers=headers,
    params=params,
)
upload_url = response.json()["href"]

with open(f"{filename}", "rb") as f:
    requests.put(upload_url, files={"file": f})

import os
import sys
import requests
from tqdm import tqdm
import time


# 1) спросить пользователя породу собаки и получить информацию о картинке с этой породой
breed = input("Введите название породы (на английском): ")
url = f"https://dog.ceo/api/breed/{breed}/images/random"
response = requests.get(url)
if response.json()["status"] != "success":
    print("Такая порода не найдена")
    sys.exit(0)
image_url = response.json()["message"]
filename = image_url.split("/")[-1]

# print(image_url)


# # 2) скачать эту картинку на компьютер
# response = requests.get(image_url)
# with open(f"{filename}", "wb") as f:
#     f.write(response.content)


# 3) создать на яндекс-диске папку для хранения картинок
yd_url = "https://cloud-api.yandex.net/v1/disk/resources"
params = {"path": "dogs"}
token = input(str("введите(вставьте) ваш токен:"))
headers = {"Authorization": f"OAuth {token}"}
response = requests.put(yd_url, params=params, headers=headers)

# # # 4) загрузить картинку с компьютера в эту папку
# # params = {'path': f'dogs/{filename}'}
# # response = requests.get('https://cloud-api.yandex.net/v1/disk/resources/upload',
# #                         headers=headers,
# #                         params=params)
# # upload_url = response.json()['href']

# # with open(f'{filename}', 'rb') as f:
# #     requests.put(upload_url, files={'file': f})


# # 4) загрузить картинку с API в эту папку


# params_1 = {'path': f'dogs/{image_url}'}
# response = requests.post('https://cloud-api.yandex.net/v1/disk/resources/upload',
#                         headers=headers,
#                         params=params_1)

yd_url_upl = "https://cloud-api.yandex.net/v1/disk/resources/upload"
params = {"path": f"dogs/{filename}", "url": image_url}
token = input(str("введите(вставьте) ваш токен:"))
headers = {"Authorization": f"OAuth {token}"}
response = requests.post(yd_url_upl, params=params, headers=headers)

# upload_url = response.json()['href']
# with open(f'{filename}', 'rb') as f:
#     requests.put(upload_url, files={'file': f})
