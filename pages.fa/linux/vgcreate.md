# vgcreate

> ایجاد گروه‌های حجم با ترکیب چند دستگاه ذخیره‌سازی انبوه.
> همچنین ببینید: `lvm`.
> اطلاعات بیشتر: <https://manned.org/vgcreate>.

- ایجاد گروه حجم جدید با دستگاه مشخص:

`sudo vgcreate {{volume_group}} {{/dev/sdXY}}`

- ایجاد گروه حجم جدید با چند دستگاه:

`sudo vgcreate {{volume_group}} {{/dev/sdXY /dev/sdXZ ...}}`

- ایجاد گروه حجم جدید با اندازهٔ گسترهٔ فیزیکی دلخواه:

`sudo vgcreate {{[-s|--physicalextentsize]}} {{8M}} {{volume_group}} {{/dev/sdXY /dev/sdXZ ...}}`
