# gio trash

> انتقال فایل‌ها به سطل زباله.
> توسط GNOME برای مدیریت زباله استفاده می‌شود.
> اطلاعات بیشتر: <https://manned.org/gio>.

- انتقال فایل‌های مشخص به سطل زباله:

`gio trash {{path/to/file_or_directory1 path/to/file_or_directory2 ...}}`

- فهرست کردن موارد سطل زباله:

`gio trash --list`

- خالی کردن سطل زباله:

`gio trash --empty`

- بازیابی یک مورد مشخص از سطل زباله با شناسهٔ آن:

`gio trash trash://{{item_id}}`
