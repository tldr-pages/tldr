# ledctl

> برنامهٔ کنترل چراغ LED محفظهٔ Intel(R).
> اطلاعات بیشتر: <https://manned.org/ledctl>.

- روشن کردن چراغ «Locate» برای دستگاه‌های مشخص:

`sudo ledctl locate={{/dev/sda,/dev/sdb,...}}`

- خاموش کردن چراغ «Locate» برای دستگاه‌های مشخص:

`sudo ledctl locate_off={{/dev/sda,/dev/sdb,...}}`

- خاموش کردن چراغ‌های «Status» و «Failure» برای دستگاه‌های مشخص:

`sudo ledctl off={{/dev/sda,/dev/sdb,...}}`

- خاموش کردن چراغ‌های «Status»، «Failure» و «Locate» برای دستگاه‌های مشخص:

`sudo ledctl normal={{/dev/sda,/dev/sdb,...}}`
