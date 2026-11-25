# duff

> ابزار یافتن فایل‌های تکراری.
> اطلاعات بیشتر: <https://github.com/elmindreda/duff>.

- یافتن بازگشتی فایل‌های تکراری:

`duff -r {{path/to/directory}}`

- فهرست کردن همهٔ فایل‌ها به‌جز یکی از هر گروه تکراری:

`duff -er {{path/to/directory}}`

- استفاده از SHA-256 به جای SHA-1:

`duff -d sha256 {{path/to/directory}}`

- مقایسهٔ بایت‌به‌بایت فایل‌ها به جای استفاده از هش:

`duff -t {{path/to/directory}}`

- در نظر گرفتن فایل‌ها و دایرکتوری‌های پنهان هنگام جست‌وجوی بازگشتی:

`duff -ar {{path/to/directory}}`
