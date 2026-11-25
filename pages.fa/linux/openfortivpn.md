# openfortivpn

> کارخواه VPN برای راهکار اختصاصی PPP+SSL VPN شرکت Fortinet.
> اطلاعات بیشتر: <https://manned.org/openfortivpn>.

- اتصال به VPN با نام کاربری و رمز عبور:

`openfortivpn {{[-u|--username]}} {{username}} {{[-p|--password]}} {{password}}`

- اتصال به VPN با فایل پیکربندی مشخص (پیش‌فرض `/etc/openfortivpn/config`):

`sudo openfortivpn {{[-c|--config]}} {{path/to/config}}`

- اتصال به VPN با تعیین میزبان و پورت:

`openfortivpn {{host}}:{{port}}`

- اعتماد به دروازهٔ مشخص با ارسال جمع sha256 گواهی آن:

`openfortivpn --trusted-cert {{sha256_sum}}`
