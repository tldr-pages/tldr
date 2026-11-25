# libtool

> اسکریپت عمومی پشتیبانی از کتابخانه که پیچیدگی استفاده از کتابخانه‌های مشترک را پشت رابطی سازگار و قابل حمل پنهان می‌کند.
> اطلاعات بیشتر: <https://www.gnu.org/software/libtool/manual/libtool.html#Invoking-libtool>.

- کامپایل فایل منبع به شیء `libtool`:

`libtool {{[c|compile]}} gcc {{[-c|--compile]}} {{path/to/source.c}} {{[-o|--output]}} {{path/to/source.lo}}`

- ایجاد کتابخانه یا فایل اجرایی:

`libtool {{[l|link]}} gcc {{[-o|--output]}} {{path/to/library.lo}} {{path/to/source.lo}}`

- تنظیم خودکار مسیر کتابخانه تا برنامهٔ دیگر بتواند از برنامه‌ها یا کتابخانه‌های نصب‌نشدهٔ تولیدشده توسط `libtool` استفاده کند:

`libtool {{[e|execute]}} gdb {{path/to/program}}`

- نصب کتابخانهٔ مشترک:

`libtool {{[i|install]}} cp {{path/to/library.la}} {{path/to/installation_directory}}`

- تکمیل نصب کتابخانه‌های `libtool` روی سیستم:

`libtool {{[f|finish]}} {{path/to/installation_directory}}`

- حذف کتابخانه‌ها یا فایل‌های اجرایی نصب‌شده:

`libtool {{[u|uninstall]}} {{path/to/installed_library.la}}`

- حذف کتابخانه‌ها یا فایل‌های اجرایی نصب‌نشده:

`libtool {{[cl|clean]}} rm {{path/to/source.lo}} {{path/to/library.la}}`
