# iwctl

> کنترل سرویس اتصال شبکهٔ `iwd`.
> همچنین ببینید: `nmcli`, `iw`.
> اطلاعات بیشتر: <https://manned.org/iwctl>.

- اجرای `iwctl` در حالت تعاملی:

`iwctl`

- نمایش ایستگاه‌های Wi-Fi:

`iwctl station list`

- جست‌وجوی شبکه‌ها با یک ایستگاه:

`iwctl station {{station}} scan`

- نمایش شبکه‌های یافت‌شده توسط ایستگاه:

`iwctl station {{station}} get-networks`

- اتصال به شبکه با یک ایستگاه؛ در صورت نیاز اطلاعات ورود درخواست می‌شود:

`iwctl station {{station}} connect {{network_name}}`

- نمایش راهنما:

`iwctl {{[-h|--help]}}`
