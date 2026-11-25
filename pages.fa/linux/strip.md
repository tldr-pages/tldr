# strip

> حذف نمادها از فایل‌های اجرایی یا شیء.
> اطلاعات بیشتر: <https://manned.org/strip>.

- جایگزینی فایل ورودی با نسخهٔ نمادزدایی‌شدهٔ آن:

`strip {{path/to/file}}`

- حذف نمادها از فایل و ذخیرهٔ خروجی در فایل مشخص:

`strip {{path/to/input_file}} -o {{path/to/output_file}}`

- حذف فقط نمادهای اشکال‌زدایی:

`strip {{[-d|--strip-debug]}} {{path/to/file.o}}`
