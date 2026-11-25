# apptainer shell

> شروع یک پوستهٔ تعاملی درون کانتینر Apptainer.
> همچنین : `apptainer exec`, `apptainer run`.
> اطلاعات بیشتر: <https://apptainer.org/docs/user/main/cli/apptainer_shell.html>.

- شروع یک پوستهٔ تعاملی درون کانتینر:

`apptainer shell {{path/to/image.sif}}`

- شروع یک پوسته با اتصال یک مسیر از میزبان به کانتینر (bind mount):

`apptainer shell {{[-B|--bind]}} {{path/to/source}}:{{path/to/destination}} {{path/to/image.sif}}`

- شروع یک پوسته با متغیرهای محیطی:

`apptainer shell --env {{variable}}={{value}} {{path/to/image.sif}}`

- شروع یک پوسته در حالت کاملاً ایزوله (سیستم فایل محصور، PID و IPC مجزا و محیط پاک):

`apptainer shell {{[-C|--containall]}} {{path/to/image.sif}}`

- شروع یک پوسته با لایهٔ موقت و قابل نوشتن سیستم فایل:

`apptainer shell --writable-tmpfs {{path/to/image.sif}}`

- شروع یک پوسته با پشتیبانی از پردازندهٔ گرافیکی NVIDIA:

`apptainer shell --nv {{path/to/image.sif}}`

- شروع یک پوسته با استفاده از یک برنامهٔ پوستهٔ مشخص:

`apptainer shell {{[-s|--shell]}} {{path/to/shell}} {{path/to/image.sif}}`

- نمایش راهنما:

`apptainer shell {{[-h|--help]}}`
