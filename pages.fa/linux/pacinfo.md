# pacinfo

> نمایش اطلاعات بسته‌های نصب‌شده.
> اطلاعات بیشتر: <https://github.com/andrewgregory/pacutils/blob/master/doc/pacinfo.pod>.

- نمایش اطلاعات بستهٔ مشخص:

`pacinfo {{package_name}}`

- غیرفعال کردن مهلت‌های سرعت پایین برای بارگیری:

`pacinfo --no-timeout {{package_name}}`

- نمایش اندازه‌ها بر حسب بایت و تاریخ‌ها به‌صورت برچسب زمانی Unix:

`pacinfo --raw {{package_name}}`

- نمایش اطلاعات اضافی بسته:

`pacinfo --verbose {{package_name}}`

- نمایش راهنما:

`pacinfo --help`

- نمایش نسخه:

`pacinfo --version`
