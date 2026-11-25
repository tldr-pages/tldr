# uci

> مدیریت فایل‌های پیکربندی OpenWrt.
> اطلاعات بیشتر: <https://openwrt.org/docs/techref/uci>.

- دریافت مقدار:

`uci get {{network.lan.ipaddr}}`

- فهرست کردن همهٔ گزینه‌ها و مقادیر آن‌ها:

`uci show {{network}}`

- تنظیم مقدار:

`uci set {{config}}.{{section}}.{{option}}={{value}}`

- افزودن بخش جدید:

`uci add {{config}} {{section}}`

- حذف بخش یا مقدار:

`uci delete {{config}}.{{section}}.{{option}}`

- ثبت تغییرات:

`uci commit {{config}}`

- دور ریختن تغییرات ثبت‌نشده:

`uci revert {{config}}`

- نمایش راهنما:

`uci`
