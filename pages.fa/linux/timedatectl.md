# timedatectl

> کنترل زمان و تاریخ سیستم.
> اطلاعات بیشتر: <https://www.freedesktop.org/software/systemd/man/latest/timedatectl.html>.

- بررسی زمان فعلی ساعت سیستم:

`timedatectl`

- تنظیم مستقیم زمان محلی ساعت سیستم:

`timedatectl set-time "{{yyyy-MM-dd hh:mm:ss}}"`

- فهرست کردن منطقه‌های زمانی موجود:

`timedatectl list-timezones`

- تنظیم منطقهٔ زمانی سیستم:

`timedatectl set-timezone {{timezone}}`

- فعال کردن همگام‌سازی پروتکل زمان شبکه (NTP):

`timedatectl set-ntp on`

- نمایش اطلاعات همگام‌سازی زمان (فقط هنگام استفاده از `systemd-timesyncd` موجود است):

`timedatectl timesync-status`

- تغییر استاندارد زمان ساعت سخت‌افزاری به زمان محلی:

`timedatectl set-local-rtc 1`
