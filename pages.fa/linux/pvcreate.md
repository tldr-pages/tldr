# pvcreate

> مقداردهی اولیهٔ دیسک یا پارتیشن برای استفاده به‌عنوان حجم فیزیکی.
> همچنین ببینید: `lvm`.
> اطلاعات بیشتر: <https://manned.org/pvcreate>.

- مقداردهی اولیهٔ حجم `/dev/sda1` برای استفاده توسط LVM:

`sudo pvcreate {{/dev/sdXY}}`

- ایجاد اجباری بدون هیچ پرسش تأیید:

`sudo pvcreate {{[-f|--force]}} {{/dev/sdXY}}`
