# ufw show

> نمایش اطلاعات دیوار آتش در حال اجرا.
> اطلاعات بیشتر: <https://manned.org/ufw>.

- نمایش قوانین افزوده‌شده در همان قالب ورود:

`sudo ufw show added`

- نمایش پورت‌های در حال گوش دادن و قوانین اعمال‌شده به آن‌ها:

`sudo ufw show listening`

- نمایش همهٔ زنجیره‌ها و قوانین `iptables` دیوار آتش در حال اجرا:

`sudo ufw show raw`

- نمایش بخش مشخص مجموعهٔ قوانین در حال اجرا:

`sudo ufw show {{builtins|before-rules|user-rules|after-rules|logging-rules}}`
