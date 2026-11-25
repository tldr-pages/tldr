# installpkg

> نصب بستهٔ Slackware.
> اطلاعات بیشتر: <https://www.slackbook.org/html/book.html#PACKAGE-MANAGEMENT-PACKAGE-UTILITIES-INSTALLPKG>.

- نصب بسته:

`sudo installpkg {{path/to/package.tgz}}`

- تولید گزارش نصب شبیه‌سازی‌شده در `stdout`:

`installpkg -warn {{path/to/package.tgz}}`

- ایجاد بسته از دایرکتوری فعلی و زیردایرکتوری‌های آن:

`installpkg -m {{package_name.tgz}}`

- نصب محتویات دایرکتوری فعلی و زیردایرکتوری‌ها به‌صورت بسته‌ای با نام مشخص:

`sudo installpkg -r {{package_name.tgz}}`
