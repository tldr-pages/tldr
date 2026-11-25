# paccheck

> بررسی بسته‌های نصب‌شده در سیستم مبتنی بر Arch برای تأیید وابستگی‌ها، صحت و سازگاری.
> اطلاعات بیشتر: <https://github.com/andrewgregory/pacutils/blob/master/doc/paccheck.pod>.

- فهرست و بررسی همهٔ بسته‌های نصب‌شده:

`paccheck`

- بررسی بسته‌های مشخص:

`paccheck {{package1 package2 ...}}`

- نمایش پیام فقط در صورت یافتن مشکل:

`paccheck --quiet`

- بررسی برآورده بودن همهٔ وابستگی‌های بسته‌ها:

`paccheck --depends`

- نمایش راهنما:

`paccheck --help`

- نمایش نسخه:

`paccheck --version`
