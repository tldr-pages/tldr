# ufw prepend

> افزودن قانون دیوار آتش به ابتدای مجموعهٔ قوانین.
> برخلاف `ufw insert` به شمارهٔ قانون موجود نیاز ندارد.
> اطلاعات بیشتر: <https://manned.org/ufw>.

- شبیه‌سازی افزودن قانون به ابتدا بدون اعمال آن:

`sudo ufw --dry-run prepend {{rule}}`

- منع همهٔ ترافیک از آدرس مبدأ، پیش از همهٔ قوانین موجود:

`sudo ufw prepend deny from {{source_address}}`

- منع همهٔ ترافیک از زیرشبکه، پیش از همهٔ قوانین موجود:

`sudo ufw prepend deny from {{192.168.0.0/24}}`

- رد ترافیک از آدرس مبدأ به پورت مشخص:

`sudo ufw prepend reject from {{source_address}} to any port {{port}}`
