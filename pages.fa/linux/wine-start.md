# wine start

> اجرای برنامه یا باز کردن سند در یک پیشوند Wine.
> بازپیاده‌سازی دستور `start` در Windows است.
> اطلاعات بیشتر: <https://gitlab.winehq.org/wine/wine/-/wikis/Commands>.

- اجرای برنامهٔ Windows:

`wine start {{path\to\program.exe}}`

- باز کردن سند با برنامهٔ مرتبط با آن:

`wine start {{path\to\document.ext}}`

- اجرای برنامه از مسیر به سبک Unix:

`wine start /unix {{path/to/program.exe}}`

- اجرای برنامه و انتظار برای خروج آن و بازگرداندن کد خروج:

`wine start /wait {{path\to\program.exe}}`

- اجرای برنامه به‌صورت کمینه یا بیشینه:

`wine start {{/min|/max}} {{path\to\program.exe}}`

- اجرای برنامه از دایرکتوری کاری مشخص:

`wine start /d {{path\to\directory}} {{path\to\program.exe}}`

- اجرای برنامه بدون باز کردن پنجرهٔ کنسول جدید:

`wine start /b {{path\to\program.exe}}`

- نمایش راهنما:

`wine start /?`
