# iw

> نمایش و تغییر دستگاه‌های بی‌سیم.
> همچنین : `nmcli`, `iwctl`.
> اطلاعات بیشتر: <https://wireless.docs.kernel.org/en/latest/en/users/documentation/iw.html>.

- پویش شبکه‌های بی‌سیم موجود:

`iw dev {{wlanX}} scan`

- پیوستن به شبکهٔ بی‌سیم باز:

`iw dev {{wlanX}} connect {{ssid}}`

- بستن اتصال فعلی:

`iw dev {{wlanX}} disconnect`

- نمایش اطلاعات اتصال فعلی:

`iw dev {{wlanX}} link`

- فهرست کردن همهٔ واسط‌های شبکهٔ بی‌سیم فیزیکی و منطقی:

`iw dev`

- فهرست کردن همهٔ قابلیت‌های بی‌سیم تمام واسط‌های سخت‌افزاری فیزیکی:

`iw phy`

- فهرست کردن اطلاعات حوزهٔ مقرراتی بی‌سیم فعلی هسته:

`iw reg get`

- نمایش راهنما:

`iw help`
