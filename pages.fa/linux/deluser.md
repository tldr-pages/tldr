# deluser

> حذف یک کاربر از سیستم.
> اطلاعات بیشتر: <https://manned.org/deluser>.

- حذف یک کاربر:

`sudo deluser {{username}}`

- حذف یک کاربر و دایرکتوری خانگی او:

`sudo deluser --remove-home {{username}}`

- حذف یک کاربر و دایرکتوری خانگی او، با پشتیبان‌گیری از فایل‌هایش در فایل `.tar.gz` در دایرکتوری مشخص:

`sudo deluser --backup-to {{path/to/backup_directory}} --remove-home {{username}}`

- حذف یک کاربر و همهٔ فایل‌های متعلق به او:

`sudo deluser --remove-all-files {{username}}`

- حذف یک کاربر از گروه بدون حذف خود کاربر:

`sudo deluser {{username}} {{group}}`
