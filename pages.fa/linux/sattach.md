# sattach

> اتصال به یک مرحلهٔ کار Slurm.
> اطلاعات بیشتر: <https://slurm.schedmd.com/sattach.html>.

- هدایت جریان‌های ورودی/خروجی (`stdout`، `stderr` و `stdin`) مرحلهٔ کار Slurm به ترمینال فعلی:

`sattach {{jobid}}.{{stepid}}`

- استفاده از ورودی کنسول فعلی به‌عنوان `stdin` وظیفهٔ مشخص:

`sattach --input-filter {{task_number}}`

- هدایت فقط `stdin`/`stderr` وظیفهٔ مشخص:

`sattach --{{output|error}}-filter {{task_number}}`
