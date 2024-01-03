import os
import uuid
from datetime import datetime as dt

from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)


def cls():
    os.system("cls" if os.name == "nt" else "clear")


with open(dotenv_path, "a") as f:
    if os.getenv("BRAND") is None:
        cls()
        print("\033[32m{}\033[0m ".format("Введите название проекта."))
        print(
            "Это название будет отображаться в строке",
            "меню и футере на страницах сайта",
            sep="\n",
        )
        br = input("-> ")
        f.writelines(f"BRAND={br}\n")

        print("\033[32m{}\033[0m ".format("Настройка блока copyright в футере сайта"))
    if os.getenv("COPYRIGHT_YEAR") is None:
        start_date = dt.utcnow().strftime("%Y")
        f.writelines(f"COPYRIGHT_YEAR={start_date}\n")

    if os.getenv("COPYRIGHT_NAME") is None:
        name = input("Введите имя для для футера:")
        f.writelines(f"COPYRIGHT_NAME={name}\n")

    if os.getenv("COPYRIGHT_LINK") is None:
        print("Введите ссылку для футера:")
        print(
            "email('something@somthing.else) или веб адрес полностью('http://anysite.any')"
        )
        link = input(">:")
        if link.startswith("http"):
            f.writelines(f"COPYRIGHT_LINK={link}\n")
        else:
            f.writelines(f"COPYRIGHT_LINK=mailto:{link}\n")

    if os.getenv("COPYRIGHT_CITY") is None:
        name = input("Введите свой город для для футера:")
        f.writelines(f"COPYRIGHT_CITY={name}\n")

    print("\033[32m{}\033[0m ".format("Генерирую SECRET_KEY..."))
    if os.getenv("SECRET_KEY") is None:
        f.writelines(f"SECRET_KEY={uuid.uuid4().hex}\n")
        print("_Ok_")
    else:
        print("SECRET_KEY уже установлен, пропускаю")

    print("\033[32m{}\033[0m ".format('Генерирую "Соль"...'))
    if os.getenv("SECURITY_PASSWORD_SALT") is None:
        f.writelines(f"SECURITY_PASSWORD_SALT={uuid.uuid4().hex}\n")
        print("_Ok_")
    else:
        print("SECURITY_PASSWORD_SALT уже установлен, пропускаю")

    if os.getenv("SQLALCHEMY_DATABASE_URI") is None:
        print(
            "\033[32m{}\033[0m ".format("Настроки подключения к базе данных Posgresql:")
        )
        login = input("Введите логин пользователя бд: ")
        passwd = input("Пароль: ")
        db = input("Название бд (по умолчанию pyprogerdb):") or "pyprogerdb"
        ip = input("Адрес бд (по умолчанию localhost)") or "localhost"
        port = input("Порт подключения: (по умолчанию 5432)") or "5432"
        f.writelines(
            f"SQLALCHEMY_DATABASE_URI=postgresql+psycopg2://{login}:{passwd}@{ip}:{port}/{db}\n"
        )
