# ifconfig

> تنظیم کننده رابط های شبکه.
> اطلاعات بیشتر: <https://net-tools.sourceforge.io/man/ifconfig.8.html>.

- نمایش تنظیمات شبکه یک کارت شبکه :

`ifconfig eth0`

- نمایش جزئیات تمامی رابط ها، مشمول رابط های غیرفعال میشود :

`ifconfig -a`

- غیرفعال کردن رابط eth0 :

`ifconfig eth0 down`

- فعال کردن رابط eth0 :

`ifconfig eth0 up`

- اختصاص آدرس ای پی به رابط eth0 :

`ifconfig eth0 {{آدرس_ای_پی}}`
