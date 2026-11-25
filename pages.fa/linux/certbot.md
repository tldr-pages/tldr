# certbot

> عامل Let’s Encrypt برای دریافت و تمدید خودکار گواهی‌های TLS.
> جانشین `letsencrypt` است.
> اطلاعات بیشتر: <https://eff-certbot.readthedocs.io/en/latest/using.html>.

- دریافت گواهی جدید از طریق تأیید با webroot، بدون نصب خودکار آن:

`sudo certbot certonly --webroot {{[-w|--webroot-path]}} {{path/to/webroot}} {{[-d|--domain]}} {{subdomain.example.com}}`

- دریافت گواهی جدید از طریق تأیید با `nginx` و نصب خودکار گواهی جدید:

`sudo certbot --nginx {{[-d|--domain]}} {{subdomain.example.com}}`

- دریافت گواهی جدید از طریق تأیید با آپاچی و نصب خودکار گواهی جدید:

`sudo certbot --apache {{[-d|--domain]}} {{subdomain.example.com}}`

- تمدید همهٔ گواهی‌های Let’s Encrypt که حداکثر تا ۳۰ روز دیگر منقضی می‌شوند (پس از آن راه‌اندازی مجدد سرورهای استفاده‌کننده از آن‌ها را فراموش نکنید):

`sudo certbot renew`

- شبیه‌سازی دریافت گواهی جدید بدون ذخیرهٔ واقعی گواهی جدید روی دیسک:

`sudo certbot --webroot {{[-w|--webroot-path]}} {{path/to/webroot}} {{[-d|--domain]}} {{subdomain.example.com}} --dry-run`

- دریافت یک گواهی آزمایشی غیرقابل اعتماد به جای آن:

`sudo certbot --webroot {{[-w|--webroot-path]}} {{path/to/webroot}} {{[-d|--domain]}} {{subdomain.example.com}} --test-cert`
