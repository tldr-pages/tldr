# ip route

> زیردستور مدیریت جدول مسیریابی IP.
> همچنین : `routel`, `ip rule`.
> اطلاعات بیشتر: <https://manned.org/ip-route>.

- نمایش جدول مسیریابی `main`:

`ip {{[r|route]}}`

- افزودن مسیر پیش‌فرض با استفاده از ارسال از طریق دروازه:

`sudo ip {{[r|route]}} {{[a|add]}} default via {{gateway_ip}}`

- افزودن مسیر پیش‌فرض با استفاده از `ethX`:

`sudo ip {{[r|route]}} {{[a|add]}} default dev {{ethX}}`

- افزودن مسیر ایستا:

`sudo ip {{[r|route]}} {{[a|add]}} {{destination_ip}} via {{gateway_ip}} dev {{ethX}}`

- حذف مسیر ایستا:

`sudo ip {{[r|route]}} {{[d|delete]}} {{destination_ip}} dev {{ethX}}`

- تغییر یا جایگزینی مسیر ایستا:

`sudo ip {{[r|route]}} {{change|replace}} {{destination_ip}} via {{gateway_ip}} dev {{ethX}}`

- نمایش مسیری که هسته برای رسیدن به آدرس IP استفاده خواهد کرد:

`ip {{[r|route]}} {{[g|get]}} {{destination_ip}}`

- نمایش جدول مسیریابی مشخص:

`ip {{[r|route]}} {{[l|list]}} {{[t|table]}} {{table_number}}`
