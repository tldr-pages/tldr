# slapt-get

> سیستمی مانند `apt` برای مدیریت بسته‌های Slackware.
> منابع بسته باید در فایل slapt-getrc پیکربندی شوند.
> اطلاعات بیشتر: <https://software.jaos.org/git/slapt-get/plain/README>.

- به‌روزرسانی فهرست بسته‌ها و نسخه‌های موجود:

`slapt-get --update`

- نصب بسته یا به‌روزرسانی آن به جدیدترین نسخهٔ موجود:

`slapt-get --install {{package}}`

- حذف بسته:

`slapt-get --remove {{package}}`

- ارتقای همهٔ بسته‌های نصب‌شده به جدیدترین نسخه‌های موجود:

`slapt-get --upgrade`

- یافتن بسته‌ها با نام، مجموعهٔ دیسک یا نسخه:

`slapt-get --search {{query}}`

- نمایش اطلاعات بسته:

`slapt-get --show {{package}}`
