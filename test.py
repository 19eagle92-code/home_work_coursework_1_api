import sys


def main():
    print("✅ Виртуальная среда работает!")
    print("✅ Проект настроен в VS Code!")

    # Проверим что мы в виртуальной среде
    import sys

    print(f"✅ Python путь: {sys.prefix}")

    # Проверим установленные пакеты
    try:
        import requests

        print(f"✅ Requests установлен: {requests.__version__}")
    except ImportError:
        print("❌ Requests не установлен")


if __name__ == "__main__":
    main()

print(f"Python: {sys.prefix}")
