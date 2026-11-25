# aptitude

> ابزار مدیریت بسته‌های دبیان و اوبونتو.
> اطلاعات بیشتر: <https://manned.org/aptitude>.

- همگام‌سازی فهرست بسته‌ها و نسخه‌های موجود؛ این دستور باید پیش از دستورهای بعدی `aptitude` اجرا شود:

`sudo aptitude update`

- نصب یک بستهٔ جدید و وابستگی‌های آن:

`sudo aptitude install {{package}}`

- جست‌وجوی یک بسته:

`aptitude search {{package}}`

- جست‌وجوی یک بستهٔ نصب‌شده (`?installed` یک عبارت جست‌وجوی `aptitude` است):

`aptitude search '?installed({{package}})'`

- حذف یک بسته و همهٔ بسته‌های وابسته به آن:

`sudo aptitude remove {{package}}`

- ارتقای بسته‌های نصب‌شده به آخرین نسخه‌های موجود:

`sudo aptitude upgrade`

- ارتقای بسته‌های نصب‌شده (مانند `aptitude upgrade`) همراه با حذف بسته‌های منسوخ و نصب بسته‌های اضافی برای برآورده کردن وابستگی‌های جدید:

`sudo aptitude full-upgrade`

- نگه داشتن یک بستهٔ نصب‌شده برای جلوگیری از ارتقای خودکار آن:

`sudo aptitude hold '?installed({{package}})'`
