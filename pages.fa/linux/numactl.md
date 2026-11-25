# numactl

> کنترل سیاست NUMA برای فرایندها یا حافظهٔ اشتراکی.
> اطلاعات بیشتر: <https://manned.org/numactl>.

- اجرای دستور روی گره ۰ با حافظهٔ تخصیص‌یافته روی گره‌های ۰ و ۱:

`numactl --cpunodebind=0 --membind=0,1 -- {{command}} {{command_arguments}}`

- اجرای دستور روی CPUهای (هسته‌های) ۰ تا ۴ و ۸ تا ۱۲ مجموعهٔ CPU فعلی:

`numactl --physcpubind=+0-4,8-12 -- {{command}} {{command_arguments}}`

- اجرای دستور با حافظهٔ درهم‌تنیده روی همهٔ CPUها:

`numactl --interleave=all -- {{command}} {{command_arguments}}`
