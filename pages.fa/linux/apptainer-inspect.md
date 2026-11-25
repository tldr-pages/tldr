# apptainer inspect

> نمایش فرادادهٔ تصاویر کانتینر Apptainer.
> اطلاعات بیشتر: <https://apptainer.org/docs/user/main/cli/apptainer_inspect.html>.

- نمایش برچسب‌های یک تصویر (پیش‌فرض):

`apptainer inspect {{path/to/image.sif}}`

- نمایش فایل تعریف استفاده‌شده برای ساخت تصویر:

`apptainer inspect {{[-d|--deffile]}} {{path/to/image.sif}}`

- نمایش اسکریپت اجرای تصویر:

`apptainer inspect {{[-r|--runscript]}} {{path/to/image.sif}}`

- نمایش متغیرهای محیطی تصویر:

`apptainer inspect {{[-e|--environment]}} {{path/to/image.sif}}`

- فهرست کردن همهٔ برنامه‌های درون کانتینر:

`apptainer inspect --list-apps {{path/to/image.sif}}`

- نمایش همهٔ داده‌های موجود در قالب JSON:

`apptainer inspect --all {{path/to/image.sif}}`

- نمایش راهنما:

`apptainer inspect {{[-h|--help]}}`
