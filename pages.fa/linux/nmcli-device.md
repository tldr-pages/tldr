# nmcli device

> مدیریت واسط‌های شبکه و برقراری اتصال‌های جدید Wi-Fi با NetworkManager.
> اطلاعات بیشتر: <https://networkmanager.pages.freedesktop.org/NetworkManager/NetworkManager/nmcli.html#device>.

- چاپ وضعیت همهٔ واسط‌های شبکه:

`nmcli {{[d|device]}}`

- چاپ نقاط دسترسی Wi-Fi موجود:

`nmcli {{[d|device]}} {{[w|wifi]}}`

- اتصال به شبکهٔ Wi-Fi با SSID مشخص (رمز عبور درخواست می‌شود):

`nmcli {{[d|device]}} {{[w|wifi]}} {{[c|connect]}} {{ssid}} {{[-a|--ask]}}`

- ایجاد نقطهٔ اتصال Wi-Fi:

`nmcli {{[d|device]}} {{[w|wifi]}} {{[ho|hotspot]}} ifname {{wlan0}} ssid "{{hotspot_ssid}}" password "{{password}}"`

- چاپ رمز عبور و کد QR شبکهٔ Wi-Fi فعلی:

`nmcli {{[d|device]}} {{[w|wifi]}} {{[s|show-password]}}`

- چاپ اطلاعات مفصل دستگاه:

`nmcli {{[d|device]}} {{[sh|show]}} {{wlan0}}`
