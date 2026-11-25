# debsecan

> تحلیلگر امنیت دبیان؛ ابزاری برای فهرست کردن آسیب‌پذیری‌های یک نصب مشخص دبیان.
> اطلاعات بیشتر: <https://manned.org/debsecan>.

- فهرست کردن بسته‌های نصب‌شدهٔ آسیب‌پذیر در میزبان فعلی:

`debsecan`

- فهرست کردن بسته‌های نصب‌شدهٔ آسیب‌پذیر یک مجموعهٔ انتشار مشخص:

`debsecan --suite {{release_code_name}}`

- فهرست کردن فقط آسیب‌پذیری‌های رفع‌شده:

`debsecan --suite {{release_code_name}} --only-fixed`

- فهرست کردن فقط آسیب‌پذیری‌های رفع‌شدهٔ نسخهٔ ناپایدار («sid») و ارسال آن به کاربر ریشه:

`debsecan --suite {{sid}} --only-fixed --format {{report}} --mailto {{root}} --update-history`

- ارتقای بسته‌های نصب‌شدهٔ آسیب‌پذیر:

`sudo apt upgrade $(debsecan --only-fixed --format {{packages}})`
