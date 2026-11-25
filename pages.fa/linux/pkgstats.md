# pkgstats

> ارسال و مشاهدهٔ آمار محبوبیت بسته‌های Arch Linux.
> اطلاعات بیشتر: <https://github.com/archlinux-de/pkgstats-cli#usage>.

- ارسال داده‌های بسته‌های نصب‌شده:

`pkgstats submit`

- مشاهدهٔ داده‌های ارسال‌شده:

`pkgstats submit {{[-d|--dump-json]}}`

- جست‌وجوی بسته‌ها:

`pkgstats search {{search_term}}`

- محدود کردن تعداد نتایج جست‌وجو (پیش‌فرض ۱۰):

`pkgstats search {{search_term}} {{[-l|--limit]}} {{count}}`

- انتخاب بسته‌ها برای مقایسه:

`pkgstats show {{package1 package2 ...}}`

- نمایش راهنما:

`pkgstats {{[-h|--help]}}`
