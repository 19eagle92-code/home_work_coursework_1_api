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
