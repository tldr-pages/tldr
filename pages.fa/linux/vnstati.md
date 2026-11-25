# vnstati

> پشتیبانی از خروجی تصویری PNG برای vnStat.
> اطلاعات بیشتر: <https://manned.org/vnstati>.

- خروجی خلاصهٔ ۲ ماه و روز اخیر و کل زمان:

`vnstati --summary --iface {{network_interface}} --output {{path/to/output.png}}`

- خروجی ۱۰ روز با بیشترین ترافیک در تمام زمان:

`vnstati --top 10 --iface {{network_interface}} --output {{path/to/output.png}}`

- خروجی آمار ماهانهٔ ترافیک ۱۲ ماه گذشته:

`vnstati --months --iface {{network_interface}} --output {{path/to/output.png}}`

- خروجی آمار ساعتی ترافیک ۲۴ ساعت گذشته:

`vnstati --hours --iface {{network_interface}} --output {{path/to/output.png}}`
