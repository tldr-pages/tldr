# steamos-finalize-install

> تکمیل نصب SteamOS با راه‌اندازی بارگذارها و اعمال به‌روزرسانی‌های سیستم.
> اطلاعات بیشتر: <https://gitlab.com/users/evlaV/projects>.

- نهایی کردن نصب:

`sudo steamos-finalize-install`

- نهایی کردن بدون به‌روزرسانی بارگذارها یا هسته:

`sudo steamos-finalize-install --no-bootloaders --no-kernel`

- رد کردن همهٔ مراحل مهاجرت:

`sudo steamos-finalize-install --no-migrate`

- تنظیم هش ریشهٔ مشخص هنگام نهایی‌سازی:

`sudo steamos-finalize-install --roothash {{hash}}`

- اجرای اجباری مراحل مهاجرت سیستم بدون توجه به محیط:

`sudo steamos-finalize-install --force`
