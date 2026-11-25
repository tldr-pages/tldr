# btrfs

> یک سیستم فایل لینوکسی مبتنی بر اصل کپی هنگام نوشتن (COW).
> برخی زیردستورها مانند `device` مستندات استفادهٔ جداگانه دارند.
> اطلاعات بیشتر: <https://btrfs.readthedocs.io/en/latest/btrfs.html>.

- ایجاد زیرحجم:

`sudo btrfs {{[su|subvolume]}} {{[c|create]}} {{path/to/subvolume}}`

- فهرست کردن زیرحجم‌ها:

`sudo btrfs {{[su|subvolume]}} {{[l|list]}} {{path/to/mount_point}}`

- نمایش اطلاعات میزان استفاده از فضا:

`sudo btrfs {{[f|filesystem]}} df {{path/to/mount_point}}`

- فعال کردن سهمیه:

`sudo btrfs {{[qu|quota]}} {{[e|enable]}} {{path/to/subvolume}}`

- نمایش سهمیه:

`sudo btrfs {{[qg|qgroup]}} {{[s|show]}} {{path/to/subvolume}}`
