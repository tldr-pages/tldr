# krfb-virtualmonitor

> ایجاد نمایشگر مجازی و فراهم کردن امکان استفاده از آن با VNC.
> اطلاعات بیشتر: <https://invent.kde.org/network/krfb>.

- ایجاد نمایشگر مجازی با ابعاد `1920x1080`:

`krfb-virtualmonitor`

- تنظیم ابعاد نمایشگر مجازی:

`krfb-virtualmonitor --resolution {{2560}}x{{1440}}`

- تنظیم نام نمایشگر:

`krfb-virtualmonitor --name {{monitor_name}}`

- تنظیم رمز عبور نمایشگر برای اتصال VNC راه دور روی پورت `5900`:

`krfb-virtualmonitor --password {{password}}`

- تنظیم رمز عبور و پورت:

`krfb-virtualmonitor --password {{password}} --port {{port}}`

- نمایش راهنما:

`krfb-virtualmonitor {{[-h|--help]}}`
