# slurmctld

> پایش سایر سرویس‌ها و منابع Slurm، پذیرش کارها و تخصیص منابع به آن‌ها.
> اطلاعات بیشتر: <https://slurm.schedmd.com/slurmctld.html>.

- پاک کردن همهٔ وضعیت‌های قبلی `slurmctld` از آخرین checkpoint:

`slurmctld -c`

- تنظیم مقدار nice سرویس به مقدار مشخص، معمولاً عدد منفی:

`slurmctld -n {{value}}`

- نوشتن پیام‌های گزارش در فایل مشخص:

`slurmctld -L {{path/to/output_file}}`

- نمایش راهنما:

`slurmctld -h`

- نمایش نسخه:

`slurmctld -V`
