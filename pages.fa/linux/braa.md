# braa

> پویشگر بسیار سریع و انبوه SNMP با امکان بررسی هم‌زمان چند میزبان.
> اطلاعات بیشتر: <https://manned.org/braa>.

- پیمایش درخت SNMP میزبان با رشتهٔ public و پرس‌وجوی همهٔ OIDهای زیر `.1.3.6`:

`braa public@{{ip_address}}:{{.1.3.6.*}}`

- پرس‌وجوی کل زیرشبکهٔ `ip_range` برای `system.sysLocation.0`:

`braa public@{{ip_range}}:{{.1.3.6.1.2.1.1.6.0}}`

- تلاش برای تنظیم مقدار `system.sysLocation.0` به یک گروه کاری مشخص:

`braa private@{{ip_address}}:{{.1.3.6.1.2.1.1.6.0}}=s'{{workgroup}}'`
