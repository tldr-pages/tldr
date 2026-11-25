# quotacheck

> پویش فایل‌سیستم برای مصرف دیسک و ایجاد، بررسی و تعمیر فایل‌های سهمیه.
> برای جلوگیری از آسیب یا از دست رفتن فایل‌های سهمیه بهتر است بررسی با سهمیه‌های غیرفعال انجام شود.
> اطلاعات بیشتر: <https://manned.org/quotacheck>.

- بررسی سهمیه‌ها در همهٔ فایل‌سیستم‌های سوارشدهٔ غیر NFS:

`sudo quotacheck --all`

- بررسی اجباری حتی با سهمیه‌های فعال (ممکن است باعث آسیب یا از دست رفتن فایل‌های سهمیه شود):

`sudo quotacheck --force {{path/to/mount_point}}`

- بررسی سهمیه‌های فایل‌سیستم مشخص در حالت اشکال‌زدایی:

`sudo quotacheck --debug {{path/to/mount_point}}`

- بررسی سهمیه‌های فایل‌سیستم مشخص همراه با نمایش پیشرفت:

`sudo quotacheck --verbose {{path/to/mount_point}}`

- بررسی سهمیه‌های کاربر:

`sudo quotacheck --user {{user}} {{path/to/mount_point}}`

- بررسی سهمیه‌های گروه:

`sudo quotacheck --group {{group}} {{path/to/mount_point}}`
