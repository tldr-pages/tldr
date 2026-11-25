# systemctl soft-reboot

> خاموش و راه‌اندازی مجدد فضای کاربر با ادامهٔ اجرای هسته.
> اطلاعات بیشتر: <https://www.freedesktop.org/software/systemd/man/latest/systemctl.html#soft-reboot>.

- انجام فوری راه‌اندازی مجدد نرم:

`systemctl soft-reboot`

- اجبار راه‌اندازی مجدد نرم:

`systemctl soft-reboot {{[-f|--force]}}`

- زمان‌بندی راه‌اندازی مجدد نرم برای زمان مشخص:

`systemctl soft-reboot --when "{{timestamp}}"`

- لغو راه‌اندازی مجدد نرم زمان‌بندی‌شده:

`systemctl soft-reboot --when cancel`
