# dmidecode

> نمایش محتوای جدول DMI (که SMBIOS نیز نامیده می‌شود) در قالب خوانا.
> همچنین ببینید: `inxi`, `lshw`, `hwinfo`.
> اطلاعات بیشتر: <https://manned.org/dmidecode>.

- نمایش همهٔ محتوای جدول DMI:

`sudo dmidecode`

- نمایش نسخهٔ BIOS:

`sudo dmidecode {{[-s|--string]}} bios-version`

- نمایش شمارهٔ سریال سیستم:

`sudo dmidecode {{[-s|--string]}} system-serial-number`

- نمایش اطلاعات BIOS:

`sudo dmidecode {{[-t|--type]}} bios`

- نمایش اطلاعات پردازنده:

`sudo dmidecode {{[-t|--type]}} processor`

- نمایش اطلاعات حافظه:

`sudo dmidecode {{[-t|--type]}} memory`
