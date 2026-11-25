# ubus

> تعامل با سرور ubusd در OpenWrt.
> اطلاعات بیشتر: <https://openwrt.org/docs/techref/ubus>.

- فهرست کردن اشیای موجود:

`ubus list`

- دریافت اطلاعات سیستم در قالب JSON:

`ubus call system board`

- گوش دادن به رویدادها:

`ubus subscribe {{event_name}}`

- نمایش راهنما:

`ubus`
