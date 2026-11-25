# systemctl cat

> نمایش محتوای کامل فایل‌های واحد همان‌گونه که systemd می‌بیند.
> اطلاعات بیشتر: <https://www.freedesktop.org/software/systemd/man/latest/systemctl.html#cat%20PATTERN%E2%80%A6>.

- نمایش محتوا و مسیر مطلق فایل واحد:

`systemctl cat {{unit}}`

- نمایش محتوای چند فایل واحد:

`systemctl cat {{unit1 unit2 ...}}`

- نمایش محتوای فایل واحد یک قالب:

`systemctl cat {{template@}}`

- نمایش محتوای فایل واحد کاربر:

`systemctl cat {{unit}} --user`
