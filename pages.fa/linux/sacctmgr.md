# sacctmgr

> مشاهده، راه‌اندازی و مدیریت حساب‌های Slurm.
> اطلاعات بیشتر: <https://slurm.schedmd.com/sacctmgr.html>.

- نمایش پیکربندی فعلی:

`sacctmgr show configuration`

- افزودن خوشه به پایگاه دادهٔ slurm:

`sacctmgr add cluster {{cluster_name}}`

- افزودن حساب به پایگاه دادهٔ slurm:

`sacctmgr add account {{account_name}} cluster={{cluster_of_account}}`

- نمایش جزئیات کاربر، ارتباط، خوشه یا حساب با قالب مشخص:

`sacctmgr show {{user|association|cluster|account}} format="Account%10" format="GrpTRES%30"`
