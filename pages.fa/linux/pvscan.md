# pvscan

> فهرست کردن همهٔ حجم‌های فیزیکی و مدیریت وضعیت آنلاین آن‌ها.
> اطلاعات بیشتر: <https://manned.org/pvscan>.

- فهرست کردن همهٔ حجم‌های فیزیکی:

`sudo pvscan`

- نمایش گروه حجمی که از حجم فیزیکی مشخص استفاده می‌کند:

`sudo pvscan --cache --listvg {{/dev/sdX}}`

- نمایش حجم‌های منطقی که از حجم فیزیکی مشخص استفاده می‌کنند:

`sudo pvscan --cache --listlvs {{/dev/sdX}}`

- نمایش اطلاعات مفصل در قالب JSON:

`sudo pvscan --reportformat json`
