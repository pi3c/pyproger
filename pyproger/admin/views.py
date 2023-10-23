from flask import abort, redirect, request, url_for
from flask_admin.contrib import sqla
from flask_ckeditor import CKEditorField
from flask_security import current_user


class MyAdminView(sqla.ModelView):
    def is_accessible(self):
        return (
            current_user.is_active
            and current_user.is_authenticated
            and current_user.has_role("superuser")
        )

    def _handle_view(self, name, **kwargs):
        if not self.is_accessible():
            if current_user.is_authenticated:
                abort(403)
            else:
                return redirect(url_for("security.login", next=request.url))


class UserView(MyAdminView):
    column_hide_backrefs = False
    column_list = (
        "email",
        "active",
        "roles",
    )
    column_labels = dict(
        first_name="Имя",
        last_name="Фамилия",
        posts="Посты",
        roles="Роли",
        email="Эл. почта",
        username="Ник",
        password="Хэш пароля",
        active="Активирован",
        confirmed_at="Подтвержден",
        last_login_at="Последний login",
        current_login_at="Текущий login",
        last_login_ip="Последний ip",
        current_login_ip="Текущий ip",
        login_count="Кол-во входов",
        create_datetime="Дата создания",
        update_datetime="Дата обновления",
    )


class RoleView(MyAdminView):
    column_list = (
        "name",
        "description",
    )
    column_labels = dict(
        name="Название",
        description="Описание",
    )


class TagView(MyAdminView):
    column_labels = dict(tag="Тэг")


class PostView(MyAdminView):
    column_list = (
        "title",
        "published",
        "tags",
    )
    column_labels = dict(
        tags="Тэги",
        slug="Слаг",
        title="Заголовок",
        header_description="description заголовок в head страницы",
        description="Краткое описание статьи",
        author="Автор",
        published="Опубликовано",
        create_datetime="Дата создания",
        update_datetime="Дата обновления",
        text="Текст",
    )

    form_overrides = dict(
        title=CKEditorField,
        description=CKEditorField,
        text=CKEditorField,
    )
    create_template = "admin/edit.html"
    edit_template = "admin/edit.html"


class PageView(MyAdminView):
    column_labels = dict(
        name="Название страницы",
        header_description="description заголовок в head страницы",
        slug="URL страницы",
        text="Содержимое страницы",
    )

    form_overrides = dict(text=CKEditorField)
    create_template = "admin/edit.html"
    edit_template = "admin/edit.html"


class HeadersView(MyAdminView):
    column_labels = dict(
        name="Название",
        description="Описание содержимого",
        content="Содержимое включаемое в header",
        enabled="Включить код в страницы сайта",
    )
    column_list = (
        "name",
        "description",
    )


class FooterLinksView(MyAdminView):
    column_labels = dict(
        name="Название",
        bootstrap_ico="Bootstrap код иконки",
        link="Ссылка",
    )
    column_list = ("name",)
