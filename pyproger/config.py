import os

FLASK_ADMIN_SWATCH = "slate"
# Create secret key so we can use sessions
# python3: secrets.token_urlsafe()
SECRET_KEY = "hxfjbcfry52"

# Create in-memory database
SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://pi3c:@localhost/pyproger"
# For debug - show every DB query
SQLALCHEMY_ECHO = False

# Flask-Security config
SECURITY_URL_PREFIX = "/admin"
SECURITY_PASSWORD_HASH = "pbkdf2_sha512"
SECURITY_PASSWORD_SALT = "ATGUOHAELKiubahiughaerGOJAEGj"
SECURITY_TRACKABLE = True

# Flask-Security URLs, overridden because they don't put a / at the end
SECURITY_LOGIN_URL = "/login/"
SECURITY_LOGOUT_URL = "/logout/"
SECURITY_REGISTER_URL = "/register/"

SECURITY_POST_LOGIN_VIEW = "/admin/"
SECURITY_POST_LOGOUT_VIEW = "/admin/"
SECURITY_POST_REGISTER_VIEW = "/admin/"
SECURITY_POST_RESET_VIEW = "/admin/"

# Flask-Security features
SECURITY_REGISTERABLE = False
SECURITY_CHANGEABLE = True
SECURITY_RECOVERABLE = False
SQLALCHEMY_TRACK_MODIFICATIONS = False

# For demo - no email
SECURITY_SEND_REGISTER_EMAIL = False
SECURITY_SEND_PASSWORD_CHANGE_EMAIL = False
SECURITY_SEND_PASSWORD_RESET_EMAIL = False
SECURITY_SEND_PASSWORD_RESET_NOTICE_EMAIL = False

# Flask-Babel
LANGUAGES = ["ru"]
BABEL_TRANSLATION_DIRECTORIES = os.path.join(os.path.curdir, "translations")
