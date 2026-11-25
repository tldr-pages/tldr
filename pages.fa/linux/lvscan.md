# lvscan

> پویش (فهرست کردن) همهٔ حجم‌های منطقی سیستم.
> بخشی از مجموعهٔ LVM (مدیر حجم منطقی).
> اطلاعات بیشتر: <https://manned.org/lvscan>.

- فهرست کردن همهٔ حجم‌های منطقی:

`sudo lvscan`

- فهرست کردن فقط حجم‌های منطقی فعال:

`sudo lvscan --active`

- فهرست کردن فقط حجم‌های منطقی غیرفعال:

`sudo lvscan --inactive`

- نمایش حجم‌های منطقی در قالب JSON:

`sudo lvscan --reportformat json`
