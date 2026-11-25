# sulogin

> ورود به‌عنوان root در حالت تک‌کاربره.
> اطلاعات بیشتر: <https://manned.org/sulogin>.

- شروع `sulogin` در کنسول پیش‌فرض:

`sudo sulogin`

- شروع `sulogin` در دستگاه TTY مشخص:

`sudo sulogin {{/dev/ttyX}}`

- تنظیم حداکثر مهلت ورود رمز عبور root بر حسب ثانیه پیش از ادامهٔ راه‌اندازی عادی:

`sudo sulogin {{[-t|--timeout]}} {{timeout}}`

- شروع پوستهٔ root به‌عنوان پوستهٔ ورود:

`sudo sulogin {{[-p|--login-shell]}}`

- اجبار پوستهٔ root بدون درخواست رمز عبور هنگام شکست روش‌های پیش‌فرض دریافت رمز:

`sudo sulogin {{[-e|--force]}}`
