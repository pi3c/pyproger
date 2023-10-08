import click
from flask import Blueprint, current_app
from flask_security.utils import hash_password

from pyproger.dbase import db, user_datastore
from pyproger.dbase.models import Role

bp_cli = Blueprint("bp_cli", __name__, cli_group=None)


@bp_cli.cli.command("create-superuser")
@click.argument("name")
def create_superuser(name):
    """Создание учетной записи админа

    Использование:
        create-superuser <name>
    Аргументы:
        <name>: Ник администратора
    """

    fname = input("Введите Ваше имя:\n")
    lname = input("Введиде Вашу фамилию:\n")
    email = input("Ваша электронная почта:\n")
    password = input("Пароль:\n")

    with current_app.app_context():

        def check_role(name):
            role = db.session.query(Role).filter(Role.name == name).one_or_none()
            return role

        user_role = check_role("user")
        if user_role is None:
            user_role = Role(name="user")
            db.session.add(user_role)

        super_user_role = check_role("superuser")
        if super_user_role is None:
            super_user_role = Role(name="superuser")
            db.session.add(super_user_role)

        db.session.commit()

        super_user = user_datastore.create_user(
            username=name,
            first_name=fname,
            last_name=lname,
            email=email,
            password=hash_password(password),
            roles=[user_role, super_user_role],
        )

        db.session.commit()
        return
