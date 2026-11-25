# apptainer run

> اجرای اسکریپت اجرای پیش‌فرض یک کانتینر Apptainer.
> اسکریپت اجرا در بخش `%runscript` فایل تعریف کانتینر مشخص می‌شود.
> همچنین : `apptainer exec`, `apptainer shell`.
> اطلاعات بیشتر: <https://apptainer.org/docs/user/main/cli/apptainer_run.html>.

- اجرای اسکریپت اجرای پیش‌فرض یک کانتینر:

`apptainer run {{path/to/image.sif}}`

- اجرا با آرگومان‌هایی که به اسکریپت اجرا داده می‌شوند:

`apptainer run {{path/to/image.sif}} {{arg1 arg2 ...}}`

- اجرا با اتصال یک مسیر از میزبان به کانتینر (bind mount):

`apptainer run {{[-B|--bind]}} {{path/to/source}}:{{path/to/destination}} {{path/to/image.sif}}`

- اجرا با متغیرهای محیطی:

`apptainer run --env {{variable}}={{value}} {{path/to/image.sif}}`

- اجرا در حالت کاملاً ایزوله (سیستم فایل محصور، PID و IPC مجزا و محیط پاک):

`apptainer run {{[-C|--containall]}} {{path/to/image.sif}}`

- اجرا با لایهٔ موقت و قابل نوشتن سیستم فایل:

`apptainer run --writable-tmpfs {{path/to/image.sif}}`

- اجرا با پشتیبانی از پردازندهٔ گرافیکی NVIDIA:

`apptainer run --nv {{path/to/image.sif}}`

- نمایش راهنما:

`apptainer run {{[-h|--help]}}`
