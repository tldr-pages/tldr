# apt-file

> جست‌وجوی فایل‌ها در بسته‌های `apt`، از جمله بسته‌هایی که هنوز نصب نشده‌اند.
> اطلاعات بیشتر: <https://manned.org/apt-file>.

- به‌روزرسانی پایگاه دادهٔ فراداده:

`sudo apt update`

- جست‌وجوی بسته‌های حاوی فایل یا مسیر مشخص‌شده:

`apt-file {{[find|search]}} {{path/to/file}}`

- فهرست کردن محتویات یک بستهٔ مشخص:

`apt-file list {{package}}`

- جست‌وجوی بسته‌های مطابق با عبارت منظم `regex`:

`apt-file {{[find|search]}} {{[-x|--regexp]}} {{regex}}`
