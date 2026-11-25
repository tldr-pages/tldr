# apptainer run-help

> نمایش راهنمای تعریف‌شده توسط کاربر برای یک تصویر کانتینر Apptainer.
> متن راهنما در بخش `%help` فایل تعریف کانتینر مشخص می‌شود.
> اطلاعات بیشتر: <https://apptainer.org/docs/user/main/cli/apptainer_run-help.html>.

- نمایش راهنمای یک کانتینر:

`apptainer run-help {{path/to/image.sif}}`

- نمایش راهنمای یک برنامهٔ مشخص درون کانتینر:

`apptainer run-help --app {{app_name}} {{path/to/image.sif}}`

- نمایش راهنما:

`apptainer run-help {{[-h|--help]}}`
