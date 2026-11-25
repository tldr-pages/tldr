# iw dev

> نمایش و تغییر دستگاه‌های بی‌سیم.
> برای فهرست کانال‌ها، فرکانس‌ها و اطلاعات مقرراتی: <https://wireless.docs.kernel.org/en/latest/en/developers/documentation/channellist.html>.
> اطلاعات بیشتر: <https://wireless.docs.kernel.org/en/latest/en/users/documentation/iw.html>.

- تنظیم دستگاه در حالت پایش (واسط باید ابتدا غیرفعال شود؛ همچنین ببینید: `ip link`):

`sudo iw dev {{wlanX}} set type monitor`

- تنظیم دستگاه در حالت مدیریت‌شده (واسط باید ابتدا غیرفعال شود):

`sudo iw dev {{wlanX}} set type managed`

- تنظیم کانال Wi-Fi دستگاه (دستگاه باید ابتدا در حالت پایش و واسط آن فعال باشد):

`sudo iw dev {{wlanX}} set channel {{channel_number}}`

- تنظیم فرکانس Wi-Fi دستگاه بر حسب مگاهرتز (دستگاه باید ابتدا در حالت پایش و واسط آن فعال باشد):

`sudo iw dev {{wlanX}} set freq {{freq_in_mhz}}`

- نمایش اطلاعات همهٔ ایستگاه‌های شناخته‌شده:

`iw dev {{wlanX}} station dump`

- ایجاد واسط مجازی در حالت پایش با آدرس MAC مشخص:

`sudo iw dev {{wlanX}} interface add "{{vif_name}}" type monitor addr {{12:34:56:aa:bb:cc}}`

- حذف واسط مجازی:

`sudo iw dev "{{vif_name}}" del`
