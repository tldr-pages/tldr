# apptainer exec

> اجرای یک دستور درون کانتینر Apptainer.
> همچنین ببینید: `apptainer run`, `apptainer shell`.
> اطلاعات بیشتر: <https://apptainer.org/docs/user/main/cli/apptainer_exec.html>.

- اجرای یک دستور درون کانتینر:

`apptainer exec {{path/to/image.sif}} {{command}}`

- اجرای یک دستور با آرگومان‌ها:

`apptainer exec {{path/to/image.sif}} {{command}} {{arg1 arg2 ...}}`

- اجرای یک دستور با اتصال یک مسیر از میزبان به کانتینر (bind mount):

`apptainer exec {{[-B|--bind]}} {{path/to/source}}:{{path/to/destination}} {{path/to/image.sif}} {{command}}`

- اجرای یک دستور با متغیرهای محیطی:

`apptainer exec --env {{variable}}={{value}} {{path/to/image.sif}} {{command}}`

- اجرای یک دستور در حالت کاملاً ایزوله (سیستم فایل محصور، PID و IPC مجزا و محیط پاک):

`apptainer exec {{[-C|--containall]}} {{path/to/image.sif}} {{command}}`

- اجرای یک دستور با لایهٔ موقت و قابل نوشتن سیستم فایل:

`apptainer exec --writable-tmpfs {{path/to/image.sif}} {{command}}`

- اجرای یک دستور با پشتیبانی از پردازندهٔ گرافیکی NVIDIA:

`apptainer exec --nv {{path/to/image.sif}} {{command}}`

- نمایش راهنما:

`apptainer exec {{[-h|--help]}}`
