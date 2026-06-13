# airmon-ng

> فعالسازی مانیتور مود بر روی دستگاه های شبکه بیسیم.
> بخشی از  `aircrack-ng`.
> اطلاعات بیشتر: <https://www.aircrack-ng.org/doku.php?id=airmon-ng>.

- فهرست کردن دستگاه های بی سیم و وضعیت آنها:

`sudo airmon-ng`

- فعالسازی مانیتور مود برای یک دستگاه خاص:

`sudo airmon-ng start {{wlan0}}`

- متوقف کردن پروسه های مزاحم که از دستگاه های بی سیم استفاده می کنند:

`sudo airmon-ng check kill`

- خاموش کردن مانیتور مود برای یک اینترفیس شبکه خاص:

`sudo airmon-ng stop {{wlan0mon}}`
