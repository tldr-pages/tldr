# mkfs.bcachefs

> ایجاد فایل‌سیستم `bcachefs` داخل پارتیشن.
> همچنین ببینید: `bcachefs`.
> اطلاعات بیشتر: <https://bcachefs-docs.readthedocs.io/en/latest/mgmt-formatting.html>.

- ایجاد فایل‌سیستم `bcachefs` داخل پارتیشن `Y` روی دستگاه `X`:

`sudo mkfs.bcachefs {{/dev/sdXY}}`

- ایجاد فایل‌سیستم `bcachefs` با برچسب حجم:

`sudo mkfs.bcachefs {{[-L|--fs_label]}} {{volume_label}} {{/dev/sdXY}}`
