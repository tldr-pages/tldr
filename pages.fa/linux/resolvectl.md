# resolvectl

> حل نام دامنه، آدرس‌های IPv4 و IPv6، رکوردهای منبع DNS و سرویس‌ها.
> توجه: `systemd-resolved.service` باید در حال اجرا باشد.
> همچنین ببینید: `dig`, `nslookup`, `host`.
> اطلاعات بیشتر: <https://www.freedesktop.org/software/systemd/man/latest/resolvectl.html>.

- نمایش تنظیمات DNS:

`resolvectl`

- حل آدرس‌های IPv4 و IPv6 برای یک یا چند دامنه:

`resolvectl query {{domain1 domain2 ...}}`

- دریافت دامنهٔ آدرس IP مشخص:

`resolvectl query {{ip_address}}`

- تخلیهٔ همهٔ حافظه‌های نهان محلی DNS:

`resolvectl flush-caches`

- نمایش آمار DNS (تراکنش‌ها، حافظهٔ نهان و نتایج DNSSEC):

`resolvectl statistics`

- دریافت رکورد MX دامنه:

`resolvectl --legend {{no}} {{[-t|--type]}} MX query {{domain}}`

- حل رکورد SRV، برای مثال `_xmpp-server._tcp gmail.com`:

`resolvectl service _{{service}}._{{protocol}} {{name}}`

- دریافت کلید TLS:

`resolvectl tlsa tcp {{domain}}:443`
