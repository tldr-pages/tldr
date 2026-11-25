# etckeeper

> ردیابی فایل‌های پیکربندی سیستم در Git.
> اطلاعات بیشتر: <https://manned.org/etckeeper>.

- راه‌اندازی مخزن Git و انجام وظایف مختلف آماده‌سازی (از `/etc` اجرا شود):

`sudo etckeeper init`

- ثبت همهٔ تغییرات `/etc` در کامیت:

`sudo etckeeper commit {{message}}`

- اجرای دستورهای دلخواه Git:

`sudo etckeeper vcs {{status}}`

- بررسی وجود تغییرات ثبت‌نشده (فقط کد خروج برمی‌گرداند):

`sudo etckeeper unclean`

- از بین بردن مخزن موجود و توقف ردیابی تغییرات:

`sudo etckeeper uninit`
