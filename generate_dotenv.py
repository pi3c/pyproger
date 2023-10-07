import os
import uuid

from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), "pyproger", ".env")
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)


with open(dotenv_path, "a") as f:
    print("Генерирую SECRET_KEY...")
    if os.getenv("SECRET_KEY") is None:
        f.writelines(f"SECRET_KEY={uuid.uuid4().hex}\n")
        print("_Ok_")
    else:
        print("SECRET_KEY уже установлен, прорускаю")

    print('Генерирую "Соль"...')
    if os.getenv("SECURITY_PASSWORD_SALT") is None:
        f.writelines(f"SECURITY_PASSWORD_SALT={uuid.uuid4().hex}\n")
        print("_Ok_")
    else:
        print("SECURITY_PASSWORD_SALT уже установлен, пропускаю")

    if os.getenv("SQLALCHEMY_DATABASE_URI") is None:
        print("Настроки подключения к базе данных Posgresql:")
        login = input("Введите логин пользователя бд: ")
        passwd = input("Пароль: ")
        db = input("Название бд (по умолчанию pyproger):") or "pyproger"
        ip = input("Адрес бд (по умолчанию localhost)") or "localhost"
        port = input("Порт подключения: (по умолчанию 5432)") or "5432"
        f.writelines(
            f"SQLALCHEMY_DATABASE_URI=postgresql+psycopg2://{login}:{passwd}@{ip}:{port}/{db}"
        )
