# xdg-user-dirs-update

> به‌روزرسانی دایرکتوری‌های کاربر XDG.
> همچنین ببینید: `xdg-user-dir`.
> اطلاعات بیشتر: <https://manned.org/xdg-user-dirs-update>.

- تغییر دایرکتوری DESKTOP مربوط به XDG به دایرکتوری مشخص:

`xdg-user-dirs-update --set DESKTOP "/{{path/to/directory}}"`

- ایجاد دایرکتوری‌های موجودنبوده:

`xdg-user-dirs-update --force`

- نوشتن نتیجه در فایل مشخص به‌جای فایل `user-dirs.dirs`:

`xdg-user-dirs-update --dummy-output "{{path/to/output_file}}" --set {{xdg_user_directory}} "/{{path/to/directory}}"`
