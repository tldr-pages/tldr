# ss

> ابزار بررسی سوکت‌ها.
> اطلاعات بیشتر: <https://manned.org/ss>.

- نمایش همهٔ سوکت‌های TCP، UDP، RAW و UNIX:

`ss {{[-a|--all]}} {{--tcp|--udp|--raw|--unix}}`

- فیلتر سوکت‌های TCP بر اساس وضعیت، فقط یا به‌جز:

`ss {{state|exclude}} {{bucket|big|connected|synchronized|...}}`

- نمایش همهٔ سوکت‌های TCP متصل به پورت HTTPS محلی (۴۴۳):

`ss {{[-t|--tcp]}} src :443`

- نمایش همهٔ سوکت‌های TCP در حال گوش دادن روی پورت محلی ۸۰۸۰:

`ss {{[-lt|--listening --tcp]}} src :8080`

- نمایش همهٔ سوکت‌های TCP همراه با فرایندهای متصل به پورت SSH راه دور:

`ss {{[-pt|--processes --tcp]}} dst :ssh`

- نمایش همهٔ سوکت‌های UDP متصل روی پورت‌های مبدأ و مقصد مشخص:

`ss {{[-u|--udp]}} 'sport == :{{source_port}} and dport == :{{destination_port}}'`

- نمایش همهٔ سوکت‌های TCP IPv4 متصل محلی در زیرشبکهٔ 192.168.0.0/16:

`ss {{[-4t|--ipv4 --tcp]}} src 192.168/16`

- پایان اتصال سوکت IPv4 یا IPv6 با IP و پورت مقصد مشخص:

`ss {{[-K|--kill]}} dst {{ip_address}} dport = {{port}}`
