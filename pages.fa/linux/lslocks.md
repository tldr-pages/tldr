# lslocks

> فهرست کردن قفل‌های محلی سیستم.
> اطلاعات بیشتر: <https://manned.org/lslocks>.

- فهرست کردن همهٔ قفل‌های محلی سیستم:

`lslocks`

- فهرست کردن قفل‌ها با سرستون‌های تعریف‌شده:

`lslocks {{[-o|--output]}} {{PID,COMMAND,PATH,...}}`

- فهرست کردن قفل‌ها با خروجی خام (بدون ستون) و بدون سرستون:

`lslocks {{[-r|--raw]}} {{[-n|--noheadings]}}`

- فهرست کردن قفل‌ها بر اساس PID ورودی:

`lslocks {{[-p|--pid]}} {{process_id}}`

- فهرست کردن قفل‌ها با خروجی JSON در `stdout`:

`lslocks {{[-J|--json]}}`
