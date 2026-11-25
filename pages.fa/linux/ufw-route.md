# ufw route

> مدیریت قوانین ترافیک مسیریابی یا ارسال‌شده از طریق میزبان.
> برای عبور ترافیک مسیریابی‌شده باید ارسال IP در هسته فعال باشد.
> اطلاعات بیشتر: <https://manned.org/ufw>.

- اجازه به مسیریابی ترافیک از یک واسط به واسط دیگر:

`sudo ufw route allow in on {{eth0}} out on {{eth1}}`

- اجازه به مسیریابی ترافیک از زیرشبکه به مقصد روی پورت و پروتکل مشخص:

`sudo ufw route allow from {{10.0.0.0/24}} to {{destination_address}} port {{port}} proto {{protocol}}`

- منع مسیریابی ترافیک به آدرس مقصد:

`sudo ufw route deny to {{destination_address}}`

- رد ترافیک مسیریابی‌شدهٔ خروجی از واسط:

`sudo ufw route reject out on {{interface}}`

- درج قانون مسیر برای آدرس مبدأ در موقعیت مشخص:

`sudo ufw route insert {{number}} {{allow|deny|reject|limit}} from {{source_address}}`

- حذف قانون مسیر:

`sudo ufw route delete {{rule}}`

- حذف قانون مسیری که ترافیک ارسال‌شده به 192.168.0.12 را منع می‌کند:

`sudo ufw route delete deny to 192.168.0.12`
