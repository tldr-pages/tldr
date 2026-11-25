# hwinfo

> بررسی سخت‌افزار موجود در سیستم.
> همچنین : `inxi`, `lshw`, `dmidecode`.
> اطلاعات بیشتر: <https://manpages.opensuse.org/hwinfo/hwinfo.8.en.html>.

- نمایش همهٔ اطلاعات سخت‌افزار موجود:

`hwinfo`

- نمایش اطلاعات یک مؤلفهٔ سخت‌افزاری مشخص:

`hwinfo --{{cpu|memory|disk|gfxcard|network|usb|pci|keyboard|mouse|monitor|sound|fingerprint|...}}`

- نمایش مختصر اطلاعات یک مؤلفهٔ سخت‌افزاری مشخص:

`hwinfo {{--component}} --short`

- نوشتن همهٔ اطلاعات سخت‌افزار در فایل:

`hwinfo --all --log {{path/to/file}}`

- نمایش راهنما:

`hwinfo --help`
