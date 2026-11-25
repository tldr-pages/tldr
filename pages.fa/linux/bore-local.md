# bore local

> شروع یک پراکسی محلی به یک سرور راه دور با استفاده از Bore.
> اطلاعات بیشتر: <https://github.com/ekzhang/bore#detailed-usage>.

- در دسترس قرار دادن یک درگاه محلی برای یک سرور راه دور Bore:

`bore local {{[-t|--to]}} {{remote_server_address}} {{local_port}}`

- در دسترس قرار دادن یک میزبان محلی مشخص به جای `localhost`:

`bore local {{[-l|--local-host]}} {{host}} {{[-t|--to]}} {{remote_server_address}} {{local_port}}`

- تعیین صریح درگاه سرور راه دور:

`bore local {{[-t|--to]}} {{remote_server_address}} {{[-p|--port]}} {{remote_port}} {{local_port}}`

- استفاده از یک مقدار محرمانه برای احراز هویت:

`bore local {{[-t|--to]}} {{remote_server_address}} {{[-s|--secret]}} {{your_secret}} {{local_port}}`

- نمایش راهنما:

`bore local {{[-h|--help]}}`
