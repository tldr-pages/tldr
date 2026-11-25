# winedbg

> اشکال‌زدای Wine برای اشکال‌زدایی برنامه‌های Windows و Winelib.
> اطلاعات بیشتر: <https://manned.org/winedbg>.

- اجرای برنامه تحت اشکال‌زدا:

`winedbg {{path/to/program.exe}}`

- اتصال به فرایند در حال اجرا با PID آن:

`winedbg {{process_id}}`

- اشکال‌زدایی برنامه از طریق پراکسی gdb (کنترل از gdb):

`winedbg --gdb {{path/to/program.exe}}`

- بارگذاری و بررسی فایل minidump خرابی:

`winedbg {{path/to/crash.mdmp}}`

- نمایش راهنما:

`winedbg --help`
