import os

# Тема оформления админ панели
FLASK_ADMIN_SWATCH = "slate"

# python3: secrets.token_urlsafe()
SECRET_KEY = "hxfjbcfry52"

# Настройки подключения к бд
SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://pi3c:@localhost/pyproger"
# For debug - show every DB query
SQLALCHEMY_ECHO = False

# Настройки Flask-Security
SECURITY_URL_PREFIX = "/admin"
SECURITY_PASSWORD_HASH = "pbkdf2_sha512"
SECURITY_PASSWORD_SALT = "ATGUOHAELKiubahiughaerGOJAEGj"
SECURITY_TRACKABLE = True

SECURITY_LOGIN_URL = "/login/"
SECURITY_LOGOUT_URL = "/logout/"
SECURITY_REGISTER_URL = "/register/"

SECURITY_POST_LOGIN_VIEW = "/admin/"
SECURITY_POST_LOGOUT_VIEW = "/admin/"
SECURITY_POST_REGISTER_VIEW = "/admin/"
SECURITY_POST_RESET_VIEW = "/admin/"

SECURITY_REGISTERABLE = False
SECURITY_CHANGEABLE = True
SECURITY_RECOVERABLE = False
SQLALCHEMY_TRACK_MODIFICATIONS = False

SECURITY_SEND_REGISTER_EMAIL = False
SECURITY_SEND_PASSWORD_CHANGE_EMAIL = False
SECURITY_SEND_PASSWORD_RESET_EMAIL = False
SECURITY_SEND_PASSWORD_RESET_NOTICE_EMAIL = False

# Настройки Flask-Babel необходимые для русификации админки
LANGUAGES = ["ru"]
BABEL_TRANSLATION_DIRECTORIES = os.path.join(os.path.curdir, "translations")

CKEDITOR_PKG_TYPE = "full"
CKEDITOR_SERVE_LOCAL = True
CKEDITOR_ENABLE_CODESNIPPET = True
CKEDITOR_CODE_THEME = "monokai_sublime"
# Настройки блога
POSTS_ON_PAGE = 6
