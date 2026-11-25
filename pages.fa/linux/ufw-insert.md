# ufw insert

> درج قانون دیوار آتش در موقعیت مشخص مجموعهٔ قوانین.
> موقعیت باید شمارهٔ قانون موجود باشد که با `ufw status numbered` نمایش داده می‌شود.
> اطلاعات بیشتر: <https://manned.org/ufw>.

- شبیه‌سازی درج قانون بدون اعمال آن:

`sudo ufw --dry-run insert {{number}} {{rule}}`

- درج قانون منع ترافیک از آدرس مبدأ در ابتدای مجموعهٔ قوانین:

`sudo ufw insert 1 deny from {{source_address}}`

- درج قانون اجازهٔ ترافیک پروتکل روی پورت در موقعیت مشخص:

`sudo ufw insert {{number}} allow {{port}}/{{protocol}}`

- درج قانون رد ترافیک از زیرشبکه به پورت:

`sudo ufw insert {{number}} reject from {{192.168.0.0/24}} to any port {{port}}`

- درج قانون محدودسازی نرخ در موقعیت مشخص:

`sudo ufw insert {{number}} limit {{22}}/{{tcp}}`
