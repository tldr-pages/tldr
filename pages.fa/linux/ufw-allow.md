# ufw allow

> اجازهٔ عبور ترافیک از دیوار آتش.
> اطلاعات بیشتر: <https://manned.org/ufw>.

- اجازه به همهٔ ترافیک روی پورت:

`sudo ufw allow {{port}}`

- اجازه به ترافیک پروتکل روی پورت:

`sudo ufw allow {{port}}/{{protocol}}`

- اجازه به ترافیک ورودی پروتکل و افزودن توضیح برای مستندسازی:

`sudo ufw allow in {{protocol}} comment '{{comment}}'`

- اجازه به همهٔ ترافیک از آدرس مبدأ:

`sudo ufw allow from {{source_address}}`

- اجازه به همهٔ ترافیک ورودی از زیرشبکهٔ 192.168.13.0/24:

`sudo ufw allow from 192.168.13.0/24`

- اجازه به ترافیک TCP از 192.168.1.12 به 192.168.1.100 روی پورت ۴۴۳:

`sudo ufw allow from 192.168.1.12 to 192.168.1.100 port 443 proto tcp`

- اجازه به همهٔ ترافیک ورودی GRE به 192.168.1.100 در واسط eth0:

`sudo ufw allow in on eth0 to 192.168.1.100 proto gre`
