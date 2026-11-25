# gpclient

> اتصال به VPN از نوع GlobalProtect در لینوکس از طریق OpenConnect.
> اطلاعات بیشتر: <https://github.com/yuezk/GlobalProtect-openconnect>.

- اتصال به VPN از نوع GlobalProtect با استفاده از سرور درگاه:

`gpclient connect {{vpn_gateway_url}}`

- قطع اتصال از سرور VPN متصل فعلی:

`gpclient disconnect`

- اجرای رابط گرافیکی مدیریت VPN:

`gpclient launch-gui`

- استفاده از راهکار OpenSSL برای عبور از خطاهای مذاکرهٔ مجدد قدیمی:

`gpclient connect --fix-openssl {{vpn_gateway_url}}`

- نادیده گرفتن خطاهای TLS هنگام اتصال:

`gpclient connect --ignore-tls-errors {{vpn_gateway_url}}`

- نمایش راهنمای هر دستور:

`gpclient help {{command}}`

- نمایش نسخه:

`gpclient --version`
