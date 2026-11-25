# pmap

> گزارش نقشهٔ حافظهٔ یک یا چند فرایند.
> اطلاعات بیشتر: <https://manned.org/pmap>.

- چاپ نقشهٔ حافظه برای شناسهٔ فرایند (PID) مشخص:

`pmap {{process_id}}`

- نمایش قالب گسترده:

`pmap --extended {{process_id}}`

- نمایش قالب دستگاه:

`pmap --device {{process_id}}`

- محدود کردن نتایج به بازهٔ آدرس حافظهٔ مشخص‌شده توسط `low` و `high`:

`pmap --range {{low}},{{high}} {{process_id}}`

- چاپ نقشهٔ حافظهٔ چند فرایند:

`pmap {{process_id1 process_id2 ...}}`
