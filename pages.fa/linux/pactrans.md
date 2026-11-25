# pactrans

> نصب، حذف و ارتقای بسته‌های ALPM.
> همچنین : `pacinstall`, `pacremove`.
> اطلاعات بیشتر: <https://github.com/andrewgregory/pacutils/blob/master/doc/pactrans.pod>.

- نصب بسته از مخزن:

`sudo pactrans --install {{package_name}}`

- حذف بسته:

`sudo pactrans --remove {{package_name}}`

- ارتقای همهٔ بسته‌های نصب‌شده:

`sudo pactrans --sysupgrade`

- نصب فایل بسته:

`sudo pactrans --file {{path/to/package.pkg.tar.zst}}`

- جایگزینی بستهٔ نصب‌شدهٔ محلی با بسته‌ای از مخزن:

`sudo pactrans local/{{package_to_remove}} {{repository_name}}/{{package_to_install}}`

- چاپ عملیات تراکنش بدون انجام آن:

`pactrans --print-only --install {{package_name}}`
