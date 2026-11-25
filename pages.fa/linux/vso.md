# vso

> مدیر بسته، به‌روزرسان سیستم و خودکارساز وظایف برای Vanilla OS.
> اطلاعات بیشتر: <https://github.com/Vanilla-OS/vanilla-system-operator>.

- بررسی به‌روزرسانی‌های سیستم میزبان:

`vso sys-upgrade check`

- ارتقای فوری سیستم میزبان:

`vso sys-upgrade upgrade --now`

- مقداردهی اولیهٔ زیرسیستم Pico (برای مدیریت بسته‌ها):

`vso pico-init`

- نصب برنامه‌ها در زیرسیستم:

`vso install {{package1 package2 ...}}`

- حذف برنامه‌ها از زیرسیستم:

`vso remove {{package1 package2 ...}}`

- ورود به پوستهٔ زیرسیستم:

`vso shell`

- اجرای برنامه‌ای از زیرسیستم:

`vso run {{package}}`

- نمایش پیکربندی VSO:

`vso config show`
