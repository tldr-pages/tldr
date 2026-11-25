# vgcfgrestore

> بازیابی پیکربندی گروه حجم (نه داده‌های کاربر) از فایل پشتیبان متنی تولیدشده توسط `vgcfgbackup`.
> اطلاعات بیشتر: <https://manned.org/vgcfgrestore>.

- بازیابی فرادادهٔ VG از آخرین پشتیبان:

`sudo vgcfgrestore {{vg_name}}`

- بازیابی فرادادهٔ VG از فایل پشتیبان مشخص:

`sudo vgcfgrestore {{[-f|--file]}} {{path/to/file}} {{vg_name}}`

- فهرست کردن همهٔ پشتیبان‌های فرادادهٔ VG:

`sudo vgcfgrestore {{[-l|--list]}} {{vg_name}}`

- فهرست کردن یک فایل پشتیبان فرادادهٔ VG:

`sudo vgcfgrestore {{[-l|--list]}} {{[-f|--file]}} {{path/to/file}} {{vg_name}}`
