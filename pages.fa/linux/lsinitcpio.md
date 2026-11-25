# lsinitcpio

> مشاهدهٔ محتویات تصویر initramfs.
> همچنین ببینید: `mkinitcpio`.
> اطلاعات بیشتر: <https://manned.org/lsinitcpio>.

- مشاهدهٔ فهرست همهٔ فایل‌ها و دایرکتوری‌های تصویر مشخص:

`lsinitcpio {{path/to/initramfs.img}}`

- استخراج تصویر در دایرکتوری فعلی:

`lsinitcpio {{[-x|--extract]}} {{path/to/initramfs.img}}`

- مشاهدهٔ اطلاعات خوانا برای انسان دربارهٔ تصویر:

`lsinitcpio {{[-a|--analyze]}} {{path/to/initramfs.img}}`
