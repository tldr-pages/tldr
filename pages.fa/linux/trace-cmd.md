# trace-cmd

> ابزار تعامل با ردیاب داخلی Ftrace هستهٔ لینوکس.
> برخی زیردستورها مانند `list`، `record` و `report` مستندات کاربرد جداگانه دارند.
> اطلاعات بیشتر: <https://manned.org/trace-cmd>.

- نمایش وضعیت سیستم ردیابی:

`sudo trace-cmd stat`

- فهرست کردن ردیاب‌های موجود:

`sudo trace-cmd list -t`

- شروع ردیابی با افزونهٔ مشخص:

`sudo trace-cmd start -p {{function|function_graph|preemptirqsoff|irqsoff|preemptoff|wakeup|...}}`

- مشاهدهٔ خروجی ردیابی:

`sudo trace-cmd show`

- توقف ردیابی با حفظ بافرها:

`sudo trace-cmd stop`

- پاک کردن بافرهای ردیابی:

`sudo trace-cmd clear`

- ضبط ردیابی:

`sudo trace-cmd record`

- نمایش ردیابی ضبط‌شده:

`sudo trace-cmd report`
