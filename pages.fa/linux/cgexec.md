# cgexec

> محدود کردن، اندازه‌گیری و کنترل منابع مصرفی فرایندها.
> انواع مختلف cgroup (یا کنترل‌کننده) مانند `cpu` و `memory` وجود دارند.
> اطلاعات بیشتر: <https://manned.org/cgexec>.

- اجرای یک فرایند در cgroup مشخص با کنترل‌کنندهٔ مشخص‌شده توسط `-g`:

`cgexec -g {{controller}}:{{cgroup_name}} {{process_name}}`
