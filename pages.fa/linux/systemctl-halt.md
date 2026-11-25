# systemctl-halt

> خاموش و متوقف کردن سیستم (توقف هستهٔ سیستم‌عامل با روشن نگه داشتن سخت‌افزار).
> همچنین ببینید: `halt`.
> اطلاعات بیشتر: <https://www.freedesktop.org/software/systemd/man/latest/systemctl.html#halt>.

- توقف سیستم:

`systemctl halt`

- توقف فوری سیستم بدون درخواست توقف صحیح از سرویس‌ها:

`systemctl halt {{[-f|--force]}}`

- توقف فوری سیستم بدون ارسال اعلان به کاربران واردشده:

`systemctl halt {{[-f|--force]}} --no-wall`

- توقف فوری سیستم بدون پایان فرایندها یا پیاده کردن فایل‌سیستم‌ها (خطرناک، ممکن است موجب از دست رفتن داده شود):

`systemctl halt {{[-ff|--force --force]}}`

- زمان‌بندی توقف در زمان مشخص (مثلاً ۲۳:۰۰):

`systemctl halt --when 23:00`

- زمان‌بندی توقف پس از مدت مشخص (مثلاً ۲ ساعت):

`systemctl halt --when +2h`

- لغو توقف زمان‌بندی‌شده:

`systemctl halt --when cancel`
