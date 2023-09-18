from flask_security.datastore import SQLAlchemyUserDatastore
from flask_security.models import fsqla
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
fsqla.FsModels.set_db_info(db)

from .models import Role, User

user_datastore = SQLAlchemyUserDatastore(db, User, Role)
