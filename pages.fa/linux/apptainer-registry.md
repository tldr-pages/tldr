# apptainer registry

> مدیریت احراز هویت در رجیستری‌های OCI/Docker.
> همچنین : `apptainer pull`, `apptainer push`.
> اطلاعات بیشتر: <https://apptainer.org/docs/user/main/cli/apptainer_registry.html>.

- فهرست کردن همهٔ اعتبارنامه‌های پیکربندی‌شدهٔ رجیستری:

`apptainer registry list`

- ورود به یک رجیستری با نام کاربری (رمز عبور درخواست می‌شود):

`apptainer registry login {{[-u|--username]}} {{username}} docker://{{registry}}`

- ورود به یک رجیستری OCI دلخواه:

`apptainer registry login {{[-u|--username]}} {{username}} oras://{{registry}}`

- ورود با نام کاربری و رمز عبور:

`apptainer registry login {{[-u|--username]}} {{username}} {{[-p|--password]}} {{password}} docker://{{registry}}`

- ورود با رمز عبور از ورودی استاندارد `stdin`:

`echo "{{password}}" | apptainer registry login {{[-u|--username]}} {{username}} --password-stdin docker://{{registry}}`

- ورود با استفاده از یک فایل احراز هویت دلخواه:

`apptainer registry login --authfile {{path/to/auth.json}} {{[-u|--username]}} {{username}} docker://{{registry}}`

- خروج از یک رجیستری:

`apptainer registry logout docker://{{registry}}`

- خروج با استفاده از یک فایل احراز هویت دلخواه:

`apptainer registry logout --authfile {{path/to/auth.json}} docker://{{registry}}`
