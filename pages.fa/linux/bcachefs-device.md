# bcachefs device

> مدیریت دستگاه‌ها در یک سیستم فایل `bcachefs` در حال اجرا.
> اطلاعات بیشتر: <https://bcachefs-docs.readthedocs.io/en/latest/mgmt-devicemanagement.html>.

- قالب‌بندی و افزودن یک دستگاه جدید به سیستم فایل موجود:

`sudo bcachefs device add --label {{group}}.{{name}} {{path/to/mount_point}} {{path/to/device}}`

- انتقال داده‌ها از یک دستگاه برای آماده‌سازی حذف آن:

`bcachefs device evacuate {{path/to/device}}`

- حذف دائمی یک دستگاه از سیستم فایل:

`bcachefs device remove {{path/to/device}}`
