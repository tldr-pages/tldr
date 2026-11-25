# cpufreq-set

> ابزاری برای تغییر تنظیمات فرکانس پردازنده.
> مقدار فرکانس باید در بازهٔ خروجی دستور `cpufreq-info -l` باشد.
> اطلاعات بیشتر: <https://manned.org/cpufreq-set>.

- تنظیم سیاست فرکانس پردازندهٔ ۱ روی «userspace»:

`sudo cpufreq-set {{[-c|--cpu]}} 1 {{[-g|--governor]}} userspace`

- تنظیم حداقل فرکانس فعلی پردازندهٔ ۱:

`sudo cpufreq-set {{[-c|--cpu]}} 1 {{[-d|--min]}} {{min_frequency}}`

- تنظیم حداکثر فرکانس فعلی پردازندهٔ ۱:

`sudo cpufreq-set {{[-c|--cpu]}} 1 {{[-u|--max]}} {{max_frequency}}`

- تنظیم فرکانس کاری فعلی پردازندهٔ ۱:

`sudo cpufreq-set {{[-c|--cpu]}} 1 {{[-f|--freq]}} {{work_frequency}}`
