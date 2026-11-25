# vcgencmd

> چاپ اطلاعات سیستم Raspberry Pi.
> اطلاعات بیشتر: <https://www.raspberrypi.com/documentation/computers/os.html#vcgencmd>.

- فهرست کردن همهٔ دستورهای موجود:

`vcgencmd commands`

- چاپ دمای فعلی CPU:

`vcgencmd measure_temp`

- چاپ ولتاژ فعلی:

`vcgencmd measure_volts`

- چاپ وضعیت محدودسازی سیستم به‌صورت الگوی بیت:

`vcgencmd get_throttled`

- چاپ پیکربندی راه‌انداز (فقط در مدل‌های Raspberry Pi 4 موجود است):

`vcgencmd bootloader_config`

- نمایش راهنما:

`vcgencmd --help`
