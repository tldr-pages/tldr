# apptainer test

> اجرای اسکریپت آزمون تعریف‌شده در یک تصویر کانتینر Apptainer.
> اسکریپت آزمون در بخش `%test` فایل تعریف کانتینر مشخص می‌شود.
> اطلاعات بیشتر: <https://apptainer.org/docs/user/main/cli/apptainer_test.html>.

- اجرای اسکریپت آزمون یک کانتینر:

`apptainer test {{path/to/image.sif}}`

- اجرای اسکریپت آزمون با اتصال یک مسیر از میزبان به کانتینر (bind mount):

`apptainer test {{[-B|--bind]}} {{path/to/source}}:{{path/to/destination}} {{path/to/image.sif}}`

- اجرای اسکریپت آزمون در حالت کاملاً ایزوله (سیستم فایل محصور، PID و IPC مجزا و محیط پاک):

`apptainer test {{[-C|--containall]}} {{path/to/image.sif}}`

- اجرای اسکریپت آزمون با لایهٔ موقت و قابل نوشتن سیستم فایل:

`apptainer test --writable-tmpfs {{path/to/image.sif}}`

- اجرای اسکریپت آزمون برای یک برنامهٔ مشخص درون کانتینر:

`apptainer test --app {{app_name}} {{path/to/image.sif}}`

- نمایش راهنما:

`apptainer test {{[-h|--help]}}`
