# chrt

> تغییر ویژگی‌های بلادرنگ یک فرایند.
> اطلاعات بیشتر: <https://manned.org/chrt>.

- نمایش ویژگی‌های یک فرایند:

`chrt {{[-p|--pid]}} {{process_id}}`

- نمایش ویژگی‌های همهٔ ریسه‌های یک فرایند:

`chrt {{[-a|--all-tasks]}} {{[-p|--pid]}} {{process_id}}`

- نمایش کمترین و بیشترین اولویت قابل استفاده با `chrt`:

`chrt {{[-m|--max]}}`

- تنظیم اولویت زمان‌بندی یک فرایند:

`chrt {{[-p|--pid]}} {{priority}} {{process_id}}`

- تنظیم سیاست زمان‌بندی یک فرایند:

`chrt --{{deadline|idle|batch|rr|fifo|other}} {{[-p|--pid]}} {{priority}} {{process_id}}`
