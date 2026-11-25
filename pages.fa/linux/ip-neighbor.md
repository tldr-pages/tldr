# ip neighbor

> زیردستور IP برای مدیریت جدول‌های همسایه، ARP و NDP.
> همچنین ببینید: `arp-scan`.
> اطلاعات بیشتر: <https://manned.org/ip-neighbour>.

- نمایش مدخل‌های جدول همسایه یا ARP:

`ip {{[n|neighbor]}}`

- حذف مدخل‌های جدول همسایه در دستگاه `ethX`:

`sudo ip {{[n|neighbor]}} {{[f|flush]}} dev {{ethX}}`

- جست‌وجوی همسایه و بازگرداندن مدخل آن:

`ip {{[n|neighbor]}} {{[g|get]}} {{lookup_ip}} dev {{ethX}}`

- افزودن یا حذف مدخل ARP برای آدرس IP همسایه در `ethX`:

`sudo ip {{[n|neighbor]}} {{add|delete}} {{ip_address}} lladdr {{mac_address}} dev {{ethX}} nud reachable`

- تغییر یا جایگزینی مدخل ARP برای آدرس IP همسایه در `ethX`:

`sudo ip {{[n|neighbor]}} {{change|replace}} {{ip_address}} lladdr {{new_mac_address}} dev {{ethX}}`

- نمایش فقط همسایه‌های IPv6 یا IPv4:

`ip {{-6|-4}} {{[n|neighbor]}}`
