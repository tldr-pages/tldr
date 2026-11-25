# setfacl

> تنظیم فهرست‌های کنترل دسترسی فایل (ACL).
> اطلاعات بیشتر: <https://manned.org/setfacl>.

- تغییر ACL فایل برای کاربر با دسترسی خواندن و نوشتن:

`setfacl {{[-m|--modify]}} u:{{username}}:rw {{path/to/file_or_directory}}`

- تغییر ACL پیش‌فرض فایل برای همهٔ کاربران:

`setfacl {{[-d|--default]}} {{[-m|--modify]}} u::rw {{path/to/file_or_directory}}`

- حذف ACL فایل برای کاربر:

`setfacl {{[-x|--remove]}} u:{{username}} {{path/to/file_or_directory}}`

- حذف همهٔ مدخل‌های ACL فایل:

`setfacl {{[-b|--remove-all]}} {{path/to/file_or_directory}}`
