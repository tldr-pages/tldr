# apptainer push

> ارسال تصاویر کانتینر به رجیستری‌های راه دور.
> همچنین ببینید: `apptainer-pull`.
> اطلاعات بیشتر: <https://apptainer.org/docs/user/main/cli/apptainer_push.html>.

- ارسال یک کانتینر به کتابخانهٔ کانتینر:

`apptainer push {{path/to/image.sif}} library://{{user/collection/container}}:{{tag}}`

- ارسال یک کانتینر به رجیستری OCI:

`apptainer push {{path/to/image.sif}} oras://{{registry/namespace/image}}:{{tag}}`

- ارسال یک کانتینر بدون امضا (صرف‌نظر از اعتبارسنجی امضا):

`apptainer push {{[-U|--allow-unsigned]}} {{path/to/image.sif}} library://{{user/collection/container}}:{{tag}}`

- ارسال یک کانتینر همراه با توضیحات (فقط برای کتابخانه):

`apptainer push {{[-D|--description]}} "{{description}}" {{path/to/image.sif}} library://{{user/collection/container}}:{{tag}}`

- نمایش راهنما:

`apptainer push {{[-h|--help]}}`
