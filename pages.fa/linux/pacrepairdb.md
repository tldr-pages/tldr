# pacrepairdb

> تعمیر مدخل‌های خراب پایگاه دادهٔ libalpm.
> اطلاعات بیشتر: <https://github.com/andrewgregory/pacutils/blob/master/doc/pacrepairdb.pod>.

- انجام تعمیر پایه روی بستهٔ مشخص:

`pacrepairdb {{package_name}}`

- به‌روزرسانی مدخل‌های پایگاه داده بدون استخراج یا حذف بسته‌ها:

`pacrepairdb {{package_name}} --dbonly`

- نمایش بسته‌های قابل تعمیر و بسته‌های حافظهٔ نهان مورد استفاده بدون ایجاد تغییر:

`pacrepairdb {{package_name}} --print-only`

- نمایش اطلاعات اضافی پیشرفت و اشکال‌زدایی:

`pacrepairdb {{package_name}} --verbose`

- نمایش راهنما:

`pacrepairdb --help`

- نمایش نسخه:

`pacrepairdb --version`
