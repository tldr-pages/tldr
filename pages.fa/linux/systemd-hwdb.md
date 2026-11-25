# systemd-hwdb

> ابزار مدیریت پایگاه دادهٔ سخت‌افزار.
> اطلاعات بیشتر: <https://www.freedesktop.org/software/systemd/man/latest/systemd-hwdb.html>.

- به‌روزرسانی پایگاه دادهٔ دودویی سخت‌افزار در `/etc/udev`:

`sudo systemd-hwdb update`

- پرس‌وجوی پایگاه دادهٔ سخت‌افزار و چاپ نتیجه برای modalias مشخص:

`systemd-hwdb query {{modalias}}`

- به‌روزرسانی پایگاه دادهٔ دودویی سخت‌افزار با کد خروج غیرصفر در هر خطای تجزیه:

`sudo systemd-hwdb {{[-s|--strict]}} update`

- به‌روزرسانی پایگاه دادهٔ دودویی سخت‌افزار در `/usr/lib/udev`:

`sudo systemd-hwdb --usr update`

- به‌روزرسانی پایگاه دادهٔ دودویی سخت‌افزار در مسیر ریشهٔ مشخص:

`systemd-hwdb {{[-r|--root]}} {{path/to/root}} update`
