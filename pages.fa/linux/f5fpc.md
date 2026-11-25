# f5fpc

> کارخواه تجاری و اختصاصی SSL VPN از BIG-IP Edge.
> اطلاعات بیشتر: <https://my.f5.com/manage/s/article/K47922841>.

- باز کردن اتصال VPN جدید:

`sudo f5fpc --start`

- باز کردن اتصال VPN جدید به میزبان مشخص:

`sudo f5fpc --start --host {{host.example.com}}`

- تعیین نام کاربری (رمز عبور از کاربر درخواست می‌شود):

`sudo f5fpc --start --host {{host.example.com}} --username {{user}}`

- نمایش وضعیت فعلی VPN:

`sudo f5fpc --info`

- قطع اتصال VPN:

`sudo f5fpc --stop`
