# sacct

> نمایش داده‌های حسابداری سرویس Slurm.
> اطلاعات بیشتر: <https://slurm.schedmd.com/sacct.html>.

- نمایش شناسه و نام کار، پارتیشن، حساب، تعداد CPUهای تخصیص‌یافته، وضعیت و کد خروج کارهای اخیر:

`sacct`

- نمایش شناسه، وضعیت و کد خروج کارهای اخیر:

`sacct {{[-b|--brief]}}`

- نمایش تخصیص‌های یک کار:

`sacct {{[-j|--jobs]}} {{job_id}} {{[-X|--allocations]}}`

- نمایش زمان سپری‌شده، نام کار، تعداد CPUهای درخواستی و حافظهٔ درخواستی یک کار:

`sacct {{[-j|--jobs]}} {{job_id}} {{[-o|--format]}} Elapsed,JobName,ReqCPUS,ReqMem`

- نمایش کارهای اخیر از یک هفته پیش تا امروز:

`sacct {{[-S|--starttime]}} $(date {{[-d|--date]}} "1 week ago" +'%F')`

- خروجی تعداد نویسهٔ بیشتر برای ویژگی:

`sacct {{[-o|--format]}} JobID,JobName%100`
