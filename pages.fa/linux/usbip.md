# usbip

> استفاده از دستگاه‌های USB از راه دور.
> اطلاعات بیشتر: <https://manned.org/usbip>.

- فهرست کردن همهٔ دستگاه‌های USB محلی و شناسهٔ گذرگاه آن‌ها:

`usbip list {{[-l|--local]}}`

- شروع سرویس `usbip` در سرور:

`systemctl start usbipd`

- اتصال دستگاه USB به `usbip` در سرور:

`sudo usbip bind {{[-b|--busid]}} {{bus_id}}`

- بارگذاری ماژول هستهٔ مورد نیاز `usbip` در کارخواه:

`sudo modprobe vhci-hcd`

- اتصال به دستگاه `usbip` در کارخواه (شناسهٔ گذرگاه همان شناسهٔ سرور است):

`sudo usbip attach {{[-r|--remote]}} {{ip_address}} {{[-b|--busid]}} {{bus_id}}`

- فهرست کردن دستگاه‌های متصل:

`usbip port`

- قطع اتصال از دستگاه:

`sudo usbip detach {{[-p|--port]}} {{port}}`

- لغو اتصال دستگاه:

`usbip unbind {{[-b|--busid]}} {{bus_id}}`
