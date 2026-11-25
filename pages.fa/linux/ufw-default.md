# ufw default

> تغییر سیاست پیش‌فرض ترافیک بر اساس جهت.
> اطلاعات بیشتر: <https://manned.org/ufw>.

- اجازه به ترافیک در جهت مشخص:

`sudo ufw default allow {{incoming|outgoing|routed}}`

- منع ترافیک در جهت مشخص:

`sudo ufw default deny {{incoming|outgoing|routed}}`

- رد ترافیک در جهت مشخص:

`sudo ufw default reject {{incoming|outgoing|routed}}`
