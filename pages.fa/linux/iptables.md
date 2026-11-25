# iptables

> پیکربندی جدول‌ها، زنجیره‌ها و قوانین دیوار آتش IPv4 هستهٔ لینوکس.
> برای تنظیم قوانین ترافیک IPv6 از `ip6tables` استفاده کنید.
> همچنین ببینید: `iptables-save`, `iptables-restore`.
> اطلاعات بیشتر: <https://manned.org/iptables>.

- مشاهدهٔ زنجیره‌ها، قوانین، شمارنده‌های بسته و بایت و شمارهٔ خطوط جدول فیلتر:

`sudo iptables {{[-vnL --line-numbers|--verbose --numeric --list --line-numbers]}}`

- تنظیم قانون سیاست زنجیره:

`sudo iptables {{[-P|--policy]}} {{chain}} {{rule}}`

- افزودن قانون IP به انتهای سیاست زنجیره:

`sudo iptables {{[-A|--append]}} {{chain}} {{[-s|--source]}} {{ip_address}} {{[-j|--jump]}} {{rule}}`

- افزودن قانون IP به انتهای سیاست زنجیره با در نظر گرفتن پروتکل و پورت:

`sudo iptables {{[-A|--append]}} {{chain}} {{[-s|--source]}} {{ip_address}} {{[-p|--protocol]}} {{tcp|udp|icmp|...}} --dport {{port}} {{[-j|--jump]}} {{rule}}`

- افزودن قانون NAT برای ترجمهٔ همهٔ ترافیک زیرشبکهٔ `192.168.0.0/24` به IP عمومی میزبان:

`sudo iptables {{[-t|--table]}} {{nat}} {{[-A|--append]}} {{POSTROUTING}} {{[-s|--source]}} {{192.168.0.0/24}} {{[-j|--jump]}} {{MASQUERADE}}`

- حذف قانون زنجیره:

`sudo iptables {{[-D|--delete]}} {{chain}} {{rule_line_number}}`
