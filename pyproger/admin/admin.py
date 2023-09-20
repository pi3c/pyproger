from flask_admin import Admin
from flask_ckeditor import CKEditor

admin = Admin(
    name="Админ панель",
    url="/admin",
    base_template="my_master.html",
    template_mode="bootstrap4",
)
