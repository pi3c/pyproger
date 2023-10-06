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