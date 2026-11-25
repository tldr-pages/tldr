# checkinstall

> ردیابی نصب محلی یک بستهٔ نرم‌افزاری و تولید یک بستهٔ دودویی قابل استفاده با مدیر بستهٔ بومی سیستم.
> اطلاعات بیشتر: <https://checkinstall.izto.org/docs.php>.

- ایجاد و نصب یک بسته با تنظیمات پیش‌فرض:

`sudo checkinstall {{[-y|--default]}}`

- ایجاد یک بسته بدون نصب آن:

`sudo checkinstall --install={{no}}`

- ایجاد یک بسته بدون مستندات:

`sudo checkinstall --nodoc`

- ایجاد یک بسته و تنظیم نام آن:

`sudo checkinstall --pkgname {{package}}`

- ایجاد یک بسته و تعیین محل ذخیرهٔ آن:

`sudo checkinstall --pakdir {{path/to/directory}}`
