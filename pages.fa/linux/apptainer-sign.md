# apptainer sign

> افزودن امضای دیجیتال به یک تصویر کانتینر SIF.
> همچنین : `apptainer-verify`.
> اطلاعات بیشتر: <https://apptainer.org/docs/user/main/cli/apptainer_sign.html>.

- امضای یک تصویر کانتینر با کلید PGP پیش‌فرض:

`apptainer sign {{path/to/image.sif}}`

- امضای یک تصویر کانتینر با فایل کلید خصوصی مشخص:

`apptainer sign --key {{path/to/private.pem}} {{path/to/image.sif}}`

- امضای یک تصویر کانتینر با شمارهٔ کلید PGP مشخص:

`apptainer sign {{[-k|--keyidx]}} {{key_index}} {{path/to/image.sif}}`

- امضای یک گروه شیء مشخص درون تصویر:

`apptainer sign {{[-g|--group-id]}} {{group_id}} {{path/to/image.sif}}`

- امضای یک شیء مشخص بر اساس شناسه درون تصویر:

`apptainer sign {{[-i|--sif-id]}} {{object_id}} {{path/to/image.sif}}`

- نمایش راهنما:

`apptainer sign {{[-h|--help]}}`
