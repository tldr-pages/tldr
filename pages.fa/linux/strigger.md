# strigger

> مشاهده یا تغییر اطلاعات محرک Slurm.
> محرک‌ها اقداماتی هستند که هنگام وقوع رویداد در خوشهٔ Slurm خودکار اجرا می‌شوند.
> اطلاعات بیشتر: <https://slurm.schedmd.com/strigger.html>.

- ثبت محرک جدید؛ اجرای برنامهٔ مشخص هنگام وقوع رویداد مشخص:

`strigger --set --{{primary_database_failure|primary_slurmdbd_failure|primary_slurmctld_acct_buffer_full|primary_slurmctld_failure|...}} {{[-p|--program]}} {{path/to/executable}}`

- اجرای برنامهٔ مشخص هنگام پایان کار مشخص:

`strigger --set {{[-j|--jobid]}} {{job_id}} {{[-f|--fini]}} {{[-p|--program]}} "{{path/to/executable}} {{argument1 argument2 ...}}"`

- مشاهدهٔ محرک‌های فعال:

`strigger --get`

- مشاهدهٔ محرک‌های فعال مرتبط با کار مشخص:

`strigger --get {{[-j|--jobid]}} {{job_id}}`

- پاک کردن محرک مشخص:

`strigger --clear {{trigger_id}}`
