# register_new_matrix_user

> ثبت کاربران جدید در سرور خانگی هنگامی که ثبت‌نام غیرفعال شده است.
> اطلاعات بیشتر: <https://manned.org/register_new_matrix_user>.

- ایجاد تعاملی کاربر:

`register_new_matrix_user --config {{path/to/homeserver.yaml}}`

- ایجاد تعاملی کاربر مدیر:

`register_new_matrix_user --config {{path/to/homeserver.yaml}} --admin`

- ایجاد غیرتعاملی کاربر مدیر (توصیه نمی‌شود):

`register_new_matrix_user --config {{path/to/homeserver.yaml}} --user {{username}} --password {{password}} --admin`
