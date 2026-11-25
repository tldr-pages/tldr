# apptainer overlay

> مدیریت تصاویر لایهٔ قابل نوشتن EXT3 برای کانتینرهای Apptainer.
> اطلاعات بیشتر: <https://apptainer.org/docs/user/main/cli/apptainer_overlay.html>.

- افزودن یک لایهٔ قابل نوشتن به تصویر SIF موجود:

`apptainer overlay create {{[-s|--size]}} {{size}} {{path/to/image.sif}}`

- ساخت یک تصویر لایهٔ مستقل و قابل نوشتن EXT3:

`apptainer overlay create {{[-s|--size]}} {{size}} {{path/to/overlay.img}}`

- ساخت یک تصویر لایهٔ تنک (sparse):

`apptainer overlay create {{[-s|--size]}} {{size}} {{[-S|--sparse]}} {{path/to/overlay.img}}`

- ساخت یک لایه برای استفاده با fakeroot:

`apptainer overlay create {{[-f|--fakeroot]}} {{[-s|--size]}} {{size}} {{path/to/overlay.img}}`

- ساخت یک لایه با یک دایرکتوری مشخص در ساختار آن:

`apptainer overlay create --create-dir {{path/to/directory}} {{path/to/overlay.img}}`

- نمایش راهنما:

`apptainer overlay {{[-h|--help]}}`
