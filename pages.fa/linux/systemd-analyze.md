# systemd-analyze

> تحلیل و اشکال‌زدایی مدیر سیستم.
> نمایش جزئیات زمان‌بندی فرایند راه‌اندازی واحدها (سرویس‌ها، نقاط اتصال، دستگاه‌ها و سوکت‌ها).
> اطلاعات بیشتر: <https://www.freedesktop.org/software/systemd/man/latest/systemd-analyze.html>.

- چاپ زمان آخرین راه‌اندازی سیستم:

`systemd-analyze`

- فهرست کردن همهٔ واحدهای در حال اجرا به ترتیب زمان مقداردهی اولیه:

`systemd-analyze blame`

- چاپ درخت زنجیرهٔ حساس زمانی واحدهای راه‌اندازی:

`systemd-analyze critical-chain`

- ایجاد فایل SVG نمایش‌دهندهٔ زمان شروع هر سرویس سیستم و برجسته کردن زمان مقداردهی اولیهٔ آن:

`systemd-analyze plot >{{path/to/file.svg}}`

- رسم گراف وابستگی و تبدیل آن به فایل SVG:

`systemd-analyze dot | dot -T {{svg}} >{{path/to/file.svg}}`

- نمایش امتیاز امنیت واحدهای در حال اجرا:

`systemd-analyze security`

- مشاهدهٔ همهٔ قوانین udev بدون نمایش توضیحات:

`systemd-analyze cat-config udev/rules.d --tldr`
