# scontrol

> مشاهدهٔ اطلاعات کارها و تغییر آن‌ها.
> اطلاعات بیشتر: <https://slurm.schedmd.com/scontrol.html>.

- نمایش اطلاعات کار:

`scontrol show job {{job_id}}`

- تعلیق فهرست جداشده با ویرگول از کارهای در حال اجرا:

`scontrol suspend {{job_id1,job_id2,...}}`

- ادامهٔ فهرست جداشده با ویرگول از کارهای معلق:

`scontrol resume {{job_id1,job_id2,...}}`

- نگه داشتن فهرست جداشده با ویرگول از کارهای صف (برای اجازهٔ زمان‌بندی کارها از دستور `release` استفاده کنید):

`scontrol hold {{job_id1,job_id2,...}}`

- آزاد کردن فهرست جداشده با ویرگول از کارهای معلق:

`scontrol release {{job_id1,job_id2,...}}`
