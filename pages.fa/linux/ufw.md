# ufw

> دیوار آتش ساده (Uncomplicated Firewall).
> رابط `iptables` برای آسان‌تر کردن پیکربندی دیوار آتش.
> برخی زیردستورها مانند `allow`، `enable` و `delete` مستندات کاربرد جداگانه دارند.
> اطلاعات بیشتر: <https://manned.org/ufw>.

- فعال یا غیرفعال کردن `ufw`:

`sudo ufw {{enable|disable}}`

- نمایش قوانین `ufw` همراه با شماره:

`sudo ufw status numbered`

- اجازه به ترافیک ورودی روی پورت ۵۴۳۲ این میزبان همراه با توضیح شناسایی سرویس:

`sudo ufw allow 5432 comment "{{Service}}"`

- اجازه فقط به ترافیک TCP از 192.168.0.4 به هر آدرس این میزبان روی پورت ۲۲:

`sudo ufw allow proto tcp from 192.168.0.4 to any port 22`

- اجازه به ترافیک هر IP در زیرشبکهٔ 192.168.0/24 روی این میزبان از پورت ۵۳ فقط در واسط eth0:

`sudo ufw allow in on eth0 from 192.168.0.0/24 to any port 53`

- منع ترافیک روی پورت ۸۰ این میزبان:

`sudo ufw deny 80`

- منع همهٔ ترافیک UDP به پورت‌های بازهٔ 8412:8500:

`sudo ufw deny proto udp from any to any port 8412:8500`

- حذف قانون مشخص؛ شمارهٔ قانون را می‌توان از دستور `ufw status numbered` دریافت کرد:

`sudo ufw delete {{rule_number}}`
