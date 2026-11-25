# timekpra

> کارخواه مدیریتی خط فرمان Timekpr-nExT، ابزاری برای مدیریت و محدود کردن زمان استفاده از رایانه برای هر حساب کاربری.
> اطلاعات بیشتر: <https://mjasnik.gitlab.io/timekpr-next/>.

- فهرست کردن همهٔ کاربران شناخته‌شده برای Timekpr-nExT:

`timekpra --getuserlist`

- نمایش پیکربندی و اطلاعات زمانی ذخیره‌شدهٔ کاربر:

`timekpra --getuserinfo {{username}}`

- نمایش پیکربندی و اطلاعات زمانی بلادرنگ کاربر:

`timekpra --getuserinfort {{username}}`

- تنظیم روزهای مجاز هفته برای کاربر (مثلاً دوشنبه تا جمعه):

`timekpra --setalloweddays {{username}} '{{1;2;3;4;5}}'`

- تنظیم محدودیت زمانی روزانه برای هر روز مجاز:

`timekpra --settimelimits {{username}} '{{2h;2h;2h;2h;3h}}'`

- تنظیم محدودیت زمانی هفتگی کاربر:

`timekpra --settimelimitweek {{username}} {{13h53m20s}}`

- افزودن، کاستن یا تنظیم زمان باقی‌ماندهٔ کاربر برای امروز:

`timekpra --settimeleft {{username}} {{+|-|=}} {{30m}}`

- تنظیم اقدام قفل پس از پایان زمان کاربر:

`timekpra --setlockouttype {{username}} {{lock|suspend|suspendwake|terminate|kill|shutdown}}`
