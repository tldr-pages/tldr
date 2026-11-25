# dhcpcd

> کارخواه DHCP.
> اطلاعات بیشتر: <https://roy.marples.name/projects/dhcpcd>.

- آزاد کردن همهٔ اجاره‌های آدرس:

`sudo dhcpcd {{[-k|--release]}}`

- درخواست اجاره‌های جدید از سرور DHCP:

`sudo dhcpcd {{[-n|--rebind]}}`

- چاپ آخرین اجارهٔ دریافت‌شده برای یک رابط مشخص:

`sudo dhcpcd {{[-U|--dumplease]}} {{interface_name}}`

- چاپ آخرین اجارهٔ دریافت‌شده برای همهٔ رابط‌ها:

`sudo dhcpcd {{[-U|--dumplease]}}`
