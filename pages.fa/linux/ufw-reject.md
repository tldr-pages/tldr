# ufw reject

> رد ترافیک از طریق دیوار آتش.
> مشابه `ufw deny` است، اما به‌جای دور ریختن بی‌صدای بسته‌ها پاسخ رد ارسال می‌کند.
> اطلاعات بیشتر: <https://manned.org/ufw>.

- رد همهٔ ترافیک روی پورت:

`sudo ufw reject {{port}}`

- رد ترافیک پروتکل روی پورت:

`sudo ufw reject {{port}}/{{protocol}}`

- رد ترافیک ورودی پروتکل و افزودن توضیح برای مستندسازی:

`sudo ufw reject in {{protocol}} comment '{{comment}}'`

- رد همهٔ ترافیک از آدرس مبدأ:

`sudo ufw reject from {{source_address}}`

- رد همهٔ ترافیک ورودی از زیرشبکهٔ 192.168.13.0/24:

`sudo ufw reject from 192.168.13.0/24`

- رد ترافیک از آدرس مبدأ به مقصد روی پورت و پروتکل مشخص:

`sudo ufw reject from {{source_address}} to {{destination_address}} port {{port}} proto {{protocol}}`

- رد همهٔ ترافیک ورودی روی واسط به IP مقصد:

`sudo ufw reject in on {{interface}} to {{destination_address}}`
