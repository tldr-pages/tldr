# scanimage

> اسکن تصاویر با API مربوط به Scanner Access Now Easy.
> اطلاعات بیشتر: <http://sane-project.org/man/scanimage.1.html>.

- فهرست کردن اسکنرهای موجود برای اطمینان از اتصال و شناسایی دستگاه مقصد:

`scanimage {{[-L|--list-devices]}}`

- اسکن تصویر و ذخیرهٔ آن در فایل:

`scanimage --format {{pnm|tiff|png|jpeg|pdf|...}} >{{path/to/new_image}}`

- تعیین دستگاه اسکن:

`scanimage {{[-d|--device]}} {{device_name}} >{{path/to/new_image}}`

- تعیین وضوح تصویر اسکن‌شده (پیش‌فرض 75dpi):

`scanimage --resolution {{300}} >{{path/to/new_image}}`
