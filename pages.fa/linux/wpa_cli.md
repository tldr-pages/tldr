# wpa_cli

> افزودن و پیکربندی واسط‌های Wi-Fi.
> اطلاعات بیشتر: <https://manned.org/wpa_cli>.

- پویش شبکه‌های موجود:

`sudo wpa_cli scan`

- نمایش نتایج پویش:

`sudo wpa_cli scan_results`

- افزودن شبکه:

`sudo wpa_cli {{[add_n|add_network]}} {{number}}`

- تنظیم SSID شبکه:

`sudo wpa_cli {{[set_n|set_network]}} {{number}} ssid "{{ssid}}"`

- فعال کردن شبکه:

`sudo wpa_cli {{[en|enable_network]}} {{number}}`

- ذخیرهٔ پیکربندی:

`sudo wpa_cli {{[sa|save_config]}}`
