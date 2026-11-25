# tlp-stat

> تولید گزارش‌های وضعیت TLP.
> همچنین ببینید: `tlp`.
> اطلاعات بیشتر: <https://linrunner.de/tlp/usage/tlp-stat>.

- تولید گزارش وضعیت همراه با پیکربندی و همهٔ تنظیمات فعال:

`sudo tlp-stat`

- نمایش اطلاعات دستگاه‌های مختلف:

`sudo tlp-stat --{{battery|disk|processor|graphics|pcie|rfkill|usb}}`

- نمایش اطلاعات مفصل دستگاه‌هایی که از آن پشتیبانی می‌کنند:

`sudo tlp-stat {{[-v|--verbose]}} --{{battery|processor|pcie|usb}}`

- نمایش پیکربندی:

`sudo tlp-stat {{[-c|--config]}}`

- پایش رویدادهای `udev` منبع تغذیه:

`sudo tlp-stat {{[-P|--pev]}}`

- نمایش اطلاعات تشخیصی منبع تغذیه:

`sudo tlp-stat --psup`

- نمایش دما و سرعت فن:

`sudo tlp-stat {{[-t|--temp]}}`

- نمایش اطلاعات عمومی سیستم:

`sudo tlp-stat {{[-s|--system]}}`
