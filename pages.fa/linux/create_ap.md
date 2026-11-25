# create_ap

> ایجاد یک نقطهٔ دسترسی (AP) روی هر کانال.
> اطلاعات بیشتر: <https://github.com/oblique/create_ap>.

- ایجاد یک شبکهٔ باز بدون عبارت عبور:

`create_ap {{wlan0}} {{eth0}} {{access_point_ssid}}`

- استفاده از عبارت عبور WPA + WPA2:

`create_ap {{wlan0}} {{eth0}} {{access_point_ssid}} {{passphrase}}`

- ایجاد یک نقطهٔ دسترسی بدون اشتراک اینترنت:

`create_ap -n {{wlan0}} {{access_point_ssid}} {{passphrase}}`

- ایجاد یک شبکهٔ پل‌شده با اشتراک اینترنت:

`create_ap -m bridge {{wlan0}} {{eth0}} {{access_point_ssid}} {{passphrase}}`

- ایجاد یک شبکهٔ پل‌شده با اشتراک اینترنت و رابط پل ازپیش‌پیکربندی‌شده:

`create_ap -m bridge {{wlan0}} {{br0}} {{access_point_ssid}} {{passphrase}}`

- ایجاد یک نقطهٔ دسترسی برای اشتراک اینترنت از همان رابط Wi-Fi:

`create_ap {{wlan0}} {{wlan0}} {{access_point_ssid}} {{passphrase}}`

- انتخاب درایور متفاوت برای آداپتور Wi-Fi:

`create_ap --driver {{wifi_adapter}} {{wlan0}} {{eth0}} {{access_point_ssid}} {{passphrase}}`
