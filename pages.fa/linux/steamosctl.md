# steamosctl

> کنترل سیستم SteamOS.
> اطلاعات بیشتر: <https://gitlab.com/evlaV/steamos-manager>.

- تغییر به حالت دسکتاپ:

`steamosctl switch-to-desktop-mode`

- تغییر به حالت بازی:

`steamosctl switch-to-game-mode`

- تغییر اینکه سیستم هنگام راه‌اندازی حالت بازی یا دسکتاپ را باز کند:

`steamosctl set-default-login-mode {{game|desktop}}`

- دریافت زمان‌بند CPU فعلی:

`steamosctl get-cpu-scheduler`

- تنظیم سیستم برای استفاده از زمان‌بند CPU مشخص:

`steamosctl set-cpu-scheduler {{none|lavd|...}}`

- نمایش نشست‌های دسکتاپ موجود:

`steamosctl get-valid-desktop-sessions`

- تنظیم نشست دسکتاپ پیش‌فرض:

`steamosctl set-default-desktop-session {{plasma.desktop|plasmax11.desktop|...}}`

- نمایش راهنما:

`steamosctl`
