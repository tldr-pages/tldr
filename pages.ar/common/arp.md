# arp

> عرض وإدارة ذاكرة التخزين المؤقت لـ ARP في النظام.
> لمزيد من التفاصيل: <https://manned.org/arp.8>.

- عرض جدول ARP الحالي:

`arp -a`

- حذف إدخال معين:

`arp -d {{address}}`

- إضافة إدخال جديد إلى جدول ARP:

`arp -s {{address}} {{mac_address}}`
