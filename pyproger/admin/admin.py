from flask_admin import Admin

admin = Admin(
    name="Админ панель",
    url="/admin",
    base_template="my_master.html",
    template_mode="bootstrap4",
)
