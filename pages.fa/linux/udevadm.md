# udevadm

> ابزار مدیریت `udev` لینوکس.
> اطلاعات بیشتر: <https://www.freedesktop.org/software/systemd/man/latest/udevadm.html>.

- پایش همهٔ رویدادهای دستگاه:

`sudo udevadm monitor`

- چاپ `uevents` ارسال‌شده توسط هسته:

`sudo udevadm monitor {{[-k|--kernel]}}`

- چاپ رویدادهای دستگاه پس از پردازش توسط `udev`:

`sudo udevadm monitor {{[-u|--udev]}}`

- فهرست کردن ویژگی‌های دستگاه `/dev/sda`:

`sudo udevadm info {{[-a|--attribute-walk]}} /dev/sda`

- بارگذاری مجدد همهٔ قوانین `udev`:

`sudo udevadm control {{[-R|--reload]}}`

- اجرای همهٔ قوانین `udev`:

`sudo udevadm trigger`

- آزمودن اجرای رویداد با شبیه‌سازی بارگذاری `/dev/sda`:

`sudo udevadm test /dev/sda`
