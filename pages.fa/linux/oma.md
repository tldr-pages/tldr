# oma

> رابط مدیریت بسته برای توزیع‌های لینوکسی مبتنی بر dpkg.
> اطلاعات بیشتر: <https://github.com/AOSC-Dev/oma#usage>.

- ورود به رابط تعاملی مدیریت بسته:

`sudo oma`

- نصب بسته:

`sudo oma install {{package_name}}`

- حذف بسته:

`sudo oma remove {{package_name}}`

- جست‌وجوی بسته:

`oma search {{keyword}}`

- نمایش اطلاعات مفصل بسته:

`oma show`

- ارتقای همهٔ بسته‌های نصب‌شده به جدیدترین نسخه:

`sudo oma upgrade`

- به‌روزرسانی فهرست بسته‌ها و نسخه‌های موجود (پیش از `oma install` و `oma upgrade` خودکار انجام می‌شود):

`sudo oma refresh`

- نمایش راهنما:

`oma help`
