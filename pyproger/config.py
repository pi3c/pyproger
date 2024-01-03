import os

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    #  app settings
    MODE: str
    
    BRAND: str
    COPYRIGHT_YEAR: int
    COPYRIGHT_NAME: str
    COPYRIGHT_LINK: str
    COPYRIGHT_CITY: str
    POSTS_ON_PAGE: int = 6

    #  sqlalchemy cofiguration
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str
    SQLALCHEMY_ECHO: bool = False
    SQLALCHEMY_TRACK_MODIFICATIONS: bool = False

    #  Flask config    
    SECRET_KEY: str
    
    #  Flask-Admin config
    FLASK_ADMIN_SWATCH: str = "slate"
    
    # Flask-Security-two config
    SECURITY_PASSWORD_SALT: str
    SECURITY_URL_PREFIX: str = "/admin"
    SECURITY_PASSWORD_HASH: str = "pbkdf2_sha512"
    SECURITY_TRACKABLE: bool = True

    SECURITY_LOGIN_URL: str = "/login/"
    SECURITY_LOGOUT_URL: str = "/logout/"
    SECURITY_REGISTER_URL: str = "/register/"

    SECURITY_POST_LOGIN_VIEW: str = "/admin/"
    SECURITY_POST_LOGOUT_VIEW: str = "/admin/"
    SECURITY_POST_REGISTER_VIEW: str = "/admin/"
    SECURITY_POST_RESET_VIEW: str = "/admin/"

    SECURITY_REGISTERABLE: bool = False
    SECURITY_CHANGEABLE: bool = True
    SECURITY_RECOVERABLE: bool = False

    SECURITY_SEND_REGISTER_EMAIL: bool = False
    SECURITY_SEND_PASSWORD_CHANGE_EMAIL: bool = False
    SECURITY_SEND_PASSWORD_RESET_EMAIL: bool = False
    SECURITY_SEND_PASSWORD_RESET_NOTICE_EMAIL: bool = False

    # Настройки Flask-Babel необходимые для русификации админки
    LANGUAGES: list = ["ru"]
    BABEL_TRANSLATION_DIRECTORIES: str = os.path.join(os.path.curdir, "translations")

    #  Flask-ckeditor config
    basedir: str = os.path.abspath(os.path.dirname(__file__))
    CKEDITOR_PKG_TYPE: str = "full"
    CKEDITOR_SERVE_LOCAL: bool = True
    CKEDITOR_ENABLE_CODESNIPPET: bool = True
    CKEDITOR_CODE_THEME: str = "monokai_sublime"
    CKEDITOR_FILE_UPLOADER: str = "upload"
    # app.config['CKEDITOR_ENABLE_CSRF'] = True  # if you want to enable CSRF protect, uncomment this line
    UPLOADED_PATH: str = os.path.join(basedir, "uploads")
    
    @property
    def DB_URL(self):
        return f"postgresql+psycopg2://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    model_config = SettingsConfigDict(env_file=".env")
    


settings = Settings()



