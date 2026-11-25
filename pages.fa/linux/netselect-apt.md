# netselect-apt

> ایجاد فایل `sources.list` برای آینهٔ Debian با کمترین تأخیر.
> اطلاعات بیشتر: <https://manned.org/netselect-apt>.

- ایجاد `sources.list` با سرور دارای کمترین تأخیر:

`sudo netselect-apt`

- تعیین شاخهٔ Debian؛ به‌طور پیش‌فرض stable استفاده می‌شود:

`sudo netselect-apt {{testing}}`

- گنجاندن بخش non-free:

`sudo netselect-apt {{[-n|--non-free]}}`

- تعیین کشور برای جست‌وجوی فهرست آینه‌ها:

`sudo netselect-apt {{[-c|--country]}} {{India}}`
