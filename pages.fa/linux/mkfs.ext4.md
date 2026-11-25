# mkfs.ext4

> ایجاد فایل‌سیستم ext4 داخل پارتیشن.
> اطلاعات بیشتر: <https://manned.org/mkfs.ext4>.

- ایجاد فایل‌سیستم ext4 داخل پارتیشن Y روی دستگاه X:

`sudo mkfs.ext4 {{/dev/sdXY}}`

- ایجاد فایل‌سیستم ext4 با برچسب حجم:

`sudo mkfs.ext4 -L {{volume_label}} {{/dev/sdXY}}`

- ایجاد فایل‌سیستم ext4 متعلق به کاربر و گروه مشخص:

`sudo mkfs.ext4 -E root_owner={{user_id}}:{{group_id}} {{/dev/sdXY}}`
