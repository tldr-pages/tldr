# snap

> مدیریت بسته‌های نرم‌افزاری مستقل «snap».
> مشابه کاربرد `apt` برای `.deb`.
> اطلاعات بیشتر: <https://manned.org/snap>.

- جست‌وجوی بسته:

`snap find {{query}}`

- نصب بسته:

`snap install {{package}}`

- به‌روزرسانی بسته:

`snap refresh {{package}}`

- به‌روزرسانی بسته به کانال دیگر (مسیر، سطح ریسک یا شاخه):

`snap refresh {{package}} --channel={{channel}}`

- به‌روزرسانی همهٔ بسته‌ها:

`snap refresh`

- نمایش اطلاعات پایهٔ نرم‌افزار snap نصب‌شده:

`snap list`

- حذف بسته:

`snap remove {{package}}`

- بررسی تغییرات اخیر snap در سیستم:

`snap changes`
