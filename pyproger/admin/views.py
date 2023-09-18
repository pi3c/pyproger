from flask import abort, redirect, request, url_for
from flask_admin.contrib import sqla
from flask_security import current_user


class MyAdminView(sqla.ModelView):
    def is_accessible(self):
        return (
            current_user.is_active
            and current_user.is_authenticated
            and current_user.has_role("superuser")
        )

    def _handle_view(self, name, **kwargs):
        """
        Override builtin _handle_view in
        order to redirect users when a
        view is not accessible.
        """
        if not self.is_accessible():
            if current_user.is_authenticated:
                # permission denied
                abort(403)
            else:
                # login
                return redirect(url_for("security.login", next=request.url))


class UserView(MyAdminView):
    column_hide_backrefs = False
    column_list = (
        "email",
        "active",
        "roles",
    )


class RoleView(MyAdminView):
    column_list = (
        "name",
        "description",
    )


class TagView(MyAdminView):
    pass


class PostView(MyAdminView):
    # form_excluded_columns = ("author", "create_datetime", "update_datetime")
    column_list = (
        "title",
        "published",
    )
    column_labels = dict(
        tags="Tags",
        title="Title",
        author="Author",
        published="Published",
        published_datetime="Pubdate",
    )
