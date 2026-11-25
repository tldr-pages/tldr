# ctrlaltdel

> ابزاری برای کنترل آنچه هنگام فشردن `<Ctrl Alt Del>` رخ می‌دهد.
> اطلاعات بیشتر: <https://manned.org/ctrlaltdel>.

- دریافت تنظیم فعلی:

`ctrlaltdel`

- تنظیم `<Ctrl Alt Del>` برای راه‌اندازی مجدد فوری بدون هیچ آماده‌سازی:

`sudo ctrlaltdel hard`

- تنظیم `<Ctrl Alt Del>` برای راه‌اندازی مجدد «معمولی» و دادن فرصت خروج به فرایندها (ارسال `SIGINT` به PID1):

`sudo ctrlaltdel soft`
