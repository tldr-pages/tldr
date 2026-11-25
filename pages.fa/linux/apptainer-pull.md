# apptainer pull

> دریافت تصاویر کانتینر از منابع راه دور.
> همچنین : `apptainer-push`.
> اطلاعات بیشتر: <https://apptainer.org/docs/user/main/cli/apptainer_pull.html>.

- دریافت یک کانتینر از Docker Hub:

`apptainer pull {{path/to/image.sif}} docker://{{image}}:{{tag}}`

- دریافت یک کانتینر از کتابخانهٔ کانتینر:

`apptainer pull {{path/to/image.sif}} library://{{user/collection/container}}:{{tag}}`

- دریافت یک کانتینر از یک رجیستری OCI:

`apptainer pull {{path/to/image.sif}} oras://{{registry/namespace/image}}:{{tag}}`

- دریافت یک کانتینر برای یک معماری مشخص:

`apptainer pull --arch {{amd64|arm64|ppc64le}} {{path/to/image.sif}} library://{{image}}:{{tag}}`

- بازنویسی اجباری یک فایل تصویر موجود:

`apptainer pull {{[-F|--force]}} {{path/to/image.sif}} docker://{{image}}:{{tag}}`

- دریافت یک کانتینر به‌صورت دایرکتوری سندباکس قابل نوشتن:

`apptainer pull --sandbox {{path/to/directory}} docker://{{image}}:{{tag}}`

- دریافت یک کانتینر بدون استفاده از حافظهٔ نهان:

`apptainer pull --disable-cache {{path/to/image.sif}} docker://{{image}}:{{tag}}`

- نمایش راهنما:

`apptainer pull {{[-h|--help]}}`
