# debman

> خواندن صفحات راهنما از بسته‌های نصب‌نشده.
> اطلاعات بیشتر: <https://manned.org/debman>.

- خواندن صفحهٔ راهنمای دستوری که توسط بستهٔ مشخص‌شده با `-p` ارائه می‌شود:

`debman -p {{package}} {{command}}`

- تعیین نسخهٔ بسته برای دانلود با `-p`:

`debman -p {{package}}={{version}} {{command}}`

- خواندن صفحهٔ راهنما در فایل `.deb` مشخص‌شده با `-f`:

`debman -f {{path/to/file.deb}} {{command}}`
