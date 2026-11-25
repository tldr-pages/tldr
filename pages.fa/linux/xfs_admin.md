# xfs_admin

> تنظیم فایل‌سیستم XFS.
> اطلاعات بیشتر: <https://manned.org/xfs_admin>.

- نمایش برچسب فایل‌سیستم:

`sudo xfs_admin {{[-l|--list]}} {{/dev/sdX}}`

- تنظیم برچسب فایل‌سیستم:

`sudo xfs_admin {{[-L|--Label]}} "{{label}}" {{/dev/sdX}}`

- نمایش UUID فایل‌سیستم:

`sudo xfs_admin {{[-u|--uuid]}} {{/dev/sdX}}`

- تنظیم UUID فایل‌سیستم (با احتیاط استفاده کنید):

`sudo xfs_admin {{[-U|--UUID]}} {{uuid}} {{/dev/sdX}}`

- تولید UUID جدید برای فایل‌سیستم:

`sudo xfs_admin {{[-U|--UUID]}} generate {{/dev/sdX}}`

- نمایش راهنما:

`xfs_admin`
