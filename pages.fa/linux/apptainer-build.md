# apptainer build

> ساخت تصاویر کانتینر Apptainer.
> اطلاعات بیشتر: <https://apptainer.org/docs/user/main/cli/apptainer_build.html>.

- ساخت یک کانتینر از فایل تعریف:

`apptainer build {{path/to/image.sif}} {{path/to/definition.def}}`

- ساخت یک کانتینر از Docker Hub:

`apptainer build {{path/to/image.sif}} docker://{{image}}:{{tag}}`

- ساخت یک کانتینر از کتابخانهٔ کانتینر:

`apptainer build {{path/to/image.sif}} library://{{user/collection/container}}:{{tag}}`

- ساخت یک دایرکتوری سندباکس قابل نوشتن به جای فایل تصویر:

`apptainer build {{[-s|--sandbox]}} {{path/to/directory}} docker://{{image}}:{{tag}}`

- ساخت یک کانتینر بدون استفاده از حافظهٔ نهان:

`apptainer build --disable-cache {{path/to/image.sif}} docker://{{image}}:{{tag}}`

- بازنویسی اجباری یک فایل تصویر موجود:

`apptainer build {{[-F|--force]}} {{path/to/image.sif}} {{path/to/definition.def}}`

- ساخت با استفاده از fakeroot برای ساخت بدون دسترسی ویژه:

`apptainer build {{[-f|--fakeroot]}} {{path/to/image.sif}} {{path/to/definition.def}}`

- نمایش راهنما:

`apptainer build {{[-h|--help]}}`
