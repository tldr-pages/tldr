# iwconfig

> پیکربندی و نمایش پارامترهای واسط شبکهٔ بی‌سیم.
> اطلاعات بیشتر: <https://manned.org/iwconfig>.

- نمایش پارامترها و آمار همهٔ واسط‌ها:

`iwconfig`

- نمایش پارامترها و آمار واسط مشخص:

`iwconfig {{interface}}`

- تنظیم ESSID (نام شبکه) واسط مشخص (مانند `eth0` یا `wlan0`):

`iwconfig {{interface}} {{new_network_name}}`

- تنظیم حالت عملکرد واسط مشخص:

`iwconfig {{interface}} mode {{Ad-Hoc|Managed|Master|Repeater|Secondary|Monitor|Auto}}`
