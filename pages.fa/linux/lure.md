# lure

> سیستم ساخت و مخزن کاربری مستقل از توزیع برای لینوکس.
> اطلاعات بیشتر: <https://github.com/lure-sh/lure/blob/master/docs/usage.md>.

- نصب بسته:

`lure {{[in|install]}} {{package}}`

- حذف بسته:

`lure {{[rm|remove]}} {{package}}`

- به‌روزرسانی بسته‌ها:

`lure {{[up|upgrade]}}`

- فهرست کردن همهٔ بسته‌های موجود:

`lure {{[ls|list]}}`

- دریافت همهٔ مخازن تغییرکرده:

`lure {{[ref|refresh]}}`

- افزودن مخزن جدید:

`lure {{[ar|addrepo]}} {{[-n|--name]}} {{repository_name}} --url {{repository_url}}`

- حذف مخزن موجود:

`lure {{[rr|removerepo]}} {{[-n|--name]}} {{repository_name}}`

- ساخت بسته:

`lure build -s {{path/to/script}}`
