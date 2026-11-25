# sdiag

> نمایش اطلاعات اجرای `slurmctld`.
> اطلاعات بیشتر: <https://slurm.schedmd.com/sdiag.html>.

- نمایش همهٔ شمارنده‌های عملکرد مرتبط با اجرای `slurmctld`:

`sdiag {{[-a|--all]}}`

- بازنشانی شمارنده‌های عملکرد مرتبط با اجرای `slurmctld`:

`sdiag {{[-r|--reset]}}`

- تعیین قالب خروجی:

`sdiag {{[-a|--all]}} --{{json|yaml}}`

- تعیین خوشه برای ارسال دستورها:

`sdiag {{[-a|--all]}} {{[-M|--cluster]}} {{cluster_name}}`
