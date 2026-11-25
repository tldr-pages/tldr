# apptainer verify

> اعتبارسنجی امضاهای دیجیتال تصاویر کانتینر SIF.
> همچنین ببینید: `apptainer-sign`.
> اطلاعات بیشتر: <https://apptainer.org/docs/user/main/cli/apptainer_verify.html>.

- اعتبارسنجی یک تصویر کانتینر با حلقه‌کلید PGP پیش‌فرض:

`apptainer verify {{path/to/image.sif}}`

- اعتبارسنجی یک تصویر کانتینر با فایل کلید عمومی مشخص:

`apptainer verify --key {{path/to/public.pem}} {{path/to/image.sif}}`

- اعتبارسنجی یک تصویر کانتینر با فایل گواهی:

`apptainer verify --certificate {{path/to/certificate.pem}} {{path/to/image.sif}}`

- اعتبارسنجی همهٔ اشیای موجود در تصویر:

`apptainer verify {{[-a|--all]}} {{path/to/image.sif}}`

- اعتبارسنجی یک گروه شیء مشخص درون تصویر:

`apptainer verify {{[-g|--group-id]}} {{group_id}} {{path/to/image.sif}}`

- اعتبارسنجی یک شیء مشخص بر اساس شناسه درون تصویر:

`apptainer verify {{[-i|--sif-id]}} {{object_id}} {{path/to/image.sif}}`

- چاپ نتایج اعتبارسنجی در قالب JSON:

`apptainer verify {{[-j|--json]}} {{path/to/image.sif}}`

- نمایش راهنما:

`apptainer verify {{[-h|--help]}}`
