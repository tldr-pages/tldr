# togglesebool

> معکوس کردن مقادیر فعلی و غیرپایدار مقادیر بولی SELinux.
> توجه: این دستور منسوخ است؛ به‌جای آن از `setsebool` استفاده کنید.
> اطلاعات بیشتر: <https://manned.org/togglesebool>.

- معکوس کردن مقادیر فعلی و غیرپایدار مقادیر بولی مشخص:

`sudo togglesebool {{virt_use_samba|virt_use_usb|...}}`

- معکوس کردن چند مقدار بولی:

`sudo togglesebool {{key1 key2 ...}}`
