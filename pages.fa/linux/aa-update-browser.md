# aa-update-browser

> به‌روزرسانی پروفایل‌های مرورگر AppArmor برای استفاده از انتزاع‌های پشتیبانی‌شده.
> بخشی از مجموعهٔ AppArmor است.
> اطلاعات بیشتر: <https://manned.org/aa-update-browser>.

- فهرست کردن پروفایل‌های انتزاع مرورگر موجود (`-l`):

`sudo aa-update-browser -l`

- نمایش تغییراتی که در یک پروفایل انجام می‌شوند، بدون اعمال آن‌ها (اجرای آزمایشی با `-d`):

`sudo aa-update-browser -d {{path/to/profile}}`

- به‌روزرسانی یک پروفایل با انتزاع‌های مشخص (`-u`):

`sudo aa-update-browser -u {{abstraction1,abstraction2,...}} {{path/to/profile}}`

- حذف همهٔ انتزاع‌ها از یک پروفایل:

`sudo aa-update-browser -u '' {{path/to/profile}}`

- نمایش راهنما:

`aa-update-browser -h`
