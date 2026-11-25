# ufw deny

> مسدود کردن ترافیک از طریق دیوار آتش.
> اطلاعات بیشتر: <https://manned.org/ufw>.

- منع همهٔ ترافیک روی پورت:

`sudo ufw deny {{port}}`

- منع ترافیک پروتکل روی پورت:

`sudo ufw deny {{port}}/{{protocol}}`

- منع ترافیک ورودی پروتکل و افزودن توضیح برای مستندسازی:

`sudo ufw deny in {{protocol}} comment '{{comment}}'`

- منع همهٔ ترافیک از آدرس مبدأ:

`sudo ufw deny from {{source_address}}`

- منع همهٔ ترافیک ورودی از زیرشبکهٔ 192.168.13.0/24:

`sudo ufw deny from 192.168.13.0/24`

- منع ترافیک UDP از 192.168.1.12 به 192.168.1.100 روی پورت ۸۰۸۰:

`sudo ufw deny from 192.168.1.12 to 192.168.1.100 port 8080 proto udp`

- منع همهٔ ترافیک ورودی IGMP به 192.168.1.100 در واسط eth0:

`sudo ufw deny in on eth0 to 192.168.1.100 proto igmp`
