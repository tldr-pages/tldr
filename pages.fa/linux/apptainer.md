# apptainer

> مدیریت کانتینرها برای محاسبات با کارایی بالا (HPC) و محاسبات علمی.
> برخی زیردستورها مانند `build`، `pull` و `push` مستندات استفادهٔ جداگانه دارند.
> اطلاعات بیشتر: <https://apptainer.org/docs/user/main/cli.html>.

- دانلود یک کانتینر از Docker Hub:

`apptainer pull {{path/to/image.sif}} docker://{{image}}:{{tag}}`

- دانلود یک کانتینر از کتابخانهٔ کانتینر:

`apptainer pull {{path/to/image.sif}} library://{{user/collection/container}}:{{tag}}`

- ساخت یک کانتینر از فایل تعریف:

`apptainer build {{path/to/image.sif}} {{path/to/definition.def}}`

- شروع یک پوستهٔ تعاملی درون کانتینر:

`apptainer shell {{path/to/image.sif}}`

- اجرای یک دستور درون کانتینر:

`apptainer exec {{path/to/image.sif}} {{command}}`

- اجرای اسکریپت اجرای پیش‌فرض یک کانتینر:

`apptainer run {{path/to/image.sif}}`

- بررسی فرادادهٔ یک کانتینر:

`apptainer inspect {{path/to/image.sif}}`

- نمایش راهنما:

`apptainer {{[-h|--help]}}`
