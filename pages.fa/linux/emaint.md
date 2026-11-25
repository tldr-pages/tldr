# emaint

> انجام وظایف نگهداری Portage.
> اطلاعات بیشتر: <https://wiki.gentoo.org/wiki/Portage#emaint>.

- همگام‌سازی مخازنی که برای همگام‌سازی خودکار تنظیم شده‌اند (پیش‌فرض بیشتر مخازن):

`sudo emaint sync {{[-a|--auto]}}`

- همگام‌سازی یک مخزن مشخص:

`sudo emaint sync {{[-r|--repo]}} {{repository}}`

- همگام‌سازی همهٔ مخازن:

`sudo emaint sync {{[-A|--allrepos]}}`

- پاک کردن فهرست ادامهٔ Portage:

`sudo emaint cleanresume {{[-f|--fix]}}`

- پاکسازی گزارش‌های Portage:

`sudo emaint logs {{[-C|--clean]}}`
