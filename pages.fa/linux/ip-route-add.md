# ip route add

> افزودن مسیر جدید شبکه.
> اطلاعات بیشتر: <https://manned.org/ip-route>.

- افزودن مسیر پیش‌فرض با استفاده از ارسال از طریق دروازه:

`sudo ip {{[r|route]}} {{[a|add]}} default via {{gateway_ip}}`

- افزودن مسیر پیش‌فرض با استفاده از `ethX`:

`sudo ip {{[r|route]}} {{[a|add]}} default dev {{ethX}}`

- افزودن مسیر ایستا:

`sudo ip {{[r|route]}} {{[a|add]}} {{destination_ip}} via {{gateway_ip}} dev {{ethX}}`

- افزودن مسیر به جدول مسیریابی مشخص:

`sudo ip {{[r|route]}} {{[a|add]}} {{destination_ip}} dev {{ethX}} {{[t|table]}} {{ip_address}}`

- وادار کردن ترافیک اینترنت به عبور از دستگاه مشخص بدون تغییر ترافیک محلی (ایجاد یک قانون نیز لازم است):

`sudo ip {{[r|route]}} {{[a|add]}} default via {{gateway_ip}} dev {{ethX}} table {{table_id}}`
