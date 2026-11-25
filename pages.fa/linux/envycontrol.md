# envycontrol

> ابزار جابه‌جایی پردازندهٔ گرافیکی برای لپ‌تاپ‌های Nvidia Optimus.
> اطلاعات بیشتر: <https://github.com/bayasdev/envycontrol#%EF%B8%8F-usage>.

- جابه‌جایی بین حالت‌های مختلف پردازندهٔ گرافیکی:

`sudo envycontrol {{[-s|--switch]}} {{nvidia|integrated|hybrid}}`

- تعیین دستی مدیر نمایش با `--dm`:

`envycontrol --dm {{gdm|gdm3|sddm|lightdm}}`

- بررسی حالت فعلی پردازندهٔ گرافیکی:

`sudo envycontrol {{[-q|--query]}}`

- بازنشانی تنظیمات:

`sudo envycontrol --reset`

- نمایش راهنما:

`envycontrol {{[-h|--help]}}`

- نمایش نسخه:

`envycontrol {{[-v|--version]}}`
