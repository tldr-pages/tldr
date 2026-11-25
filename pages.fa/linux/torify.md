# torify

> مسیریابی ترافیک شبکه از طریق شبکهٔ Tor.
> توجه: این دستور منسوخ است؛ به‌جای آن از `torsocks` استفاده کنید. `torify` اکنون واسط سازگار با گذشتهٔ `torsocks` است.
> اطلاعات بیشتر: <https://manned.org/torify>.

- مسیریابی ترافیک از طریق Tor:

`torify {{command}}`

- تغییر وضعیت Tor در پوسته:

`torify {{on|off}}`

- ایجاد پوستهٔ مجهز به Tor:

`torify --shell`

- بررسی پوستهٔ مجهز به Tor:

`torify show`

- تعیین فایل پیکربندی Tor:

`torify -c {{config_file}} {{command}}`

- استفاده از پراکسی SOCKS مشخص Tor:

`torify -P {{proxy}} {{command}}`

- هدایت خروجی به فایل:

`torify {{command}} >{{path/to/output}}`
