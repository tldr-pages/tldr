# setxkbmap

> تنظیم صفحه‌کلید با افزونهٔ X Keyboard.
> اطلاعات بیشتر: <https://manned.org/setxkbmap>.

- تنظیم صفحه‌کلید به AZERTY فرانسوی:

`setxkbmap {{fr}}`

- تنظیم چند چیدمان صفحه‌کلید، گونه‌های آن‌ها و گزینهٔ جابه‌جایی:

`setxkbmap -layout {{us,de}} -variant {{,qwerty}} -option '{{grp:alt_caps_toggle}}'`

- فهرست کردن همهٔ چیدمان‌ها:

`localectl list-x11-keymap-layouts`

- فهرست کردن گونه‌های چیدمان:

`localectl list-x11-keymap-variants {{de}}`

- فهرست کردن گزینه‌های جابه‌جایی موجود:

`localectl list-x11-keymap-options | grep grp:`

- نمایش راهنما:

`setxkbmap -help`
