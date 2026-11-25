# turbostat

> گزارش توپولوژی، فرکانس، دما، توان و آمار بی‌کاری پردازنده.
> اطلاعات بیشتر: <https://manned.org/turbostat>.

- نمایش آمار هر ۵ ثانیه:

`sudo turbostat`

- نمایش آمار هر تعداد ثانیهٔ مشخص:

`sudo turbostat {{[-i|--interval]}} {{n_seconds}}`

- رمزگشایی و چاپ نکردن اطلاعات سربرگ پیکربندی سیستم:

`sudo turbostat --quiet`

- نمایش اطلاعات مفید CPU هر ۱ ثانیه، بدون اطلاعات سربرگ:

`sudo turbostat --quiet {{[-i|--interval]}} 1 --cpu 0-{{cpu_thread_count}} --show "PkgWatt","Busy%","Core","CoreTmp","Thermal"`

- نمایش راهنما:

`turbostat --help`
