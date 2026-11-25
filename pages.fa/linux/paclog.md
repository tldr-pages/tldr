# paclog

> فیلتر کردن مدخل‌های گزارش pacman.
> اطلاعات بیشتر: <https://github.com/andrewgregory/pacutils/blob/master/doc/paclog.pod>.

- نمایش کل گزارش pacman:

`paclog`

- نمایش مدخل‌های خط فرمان ثبت‌شده به سبک pacman:

`paclog --commandline`

- نمایش رویدادهای گزارش برای بستهٔ مشخص:

`paclog --package {{package_name}}`

- نمایش عملیات بسته از نوع مشخص:

`paclog --action {{install|reinstall|upgrade|downgrade|remove|all}}`

- نمایش فقط خطاها، هشدارها و یادداشت‌ها:

`paclog --warnings`

- نمایش فهرست بسته‌های نصب‌شده مطابق گزارش:

`paclog --pkglist`

- نمایش راهنما:

`paclog --help`

- نمایش نسخه:

`paclog --version`
