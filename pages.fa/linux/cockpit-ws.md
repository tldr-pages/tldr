# cockpit-ws

> برقراری ارتباط بین برنامهٔ مرورگر و ابزارها و سرویس‌های مختلف پیکربندی مانند `cockpit-bridge`.
> اطلاعات بیشتر: <https://cockpit-project.org/guide/latest/cockpit-ws.8.html>.

- شروع با احراز هویت از طریق SSH در `127.0.0.1` و فعال بودن درگاه `22`:

`cockpit-ws --local-ssh`

- شروع یک سرور HTTP روی درگاه مشخص:

`cockpit-ws --port {{port}}`

- شروع و اتصال به یک آدرس IP مشخص (پیش‌فرض `0.0.0.0` است):

`cockpit-ws --address {{ip_address}}`

- شروع بدون TLS:

`cockpit-ws --no-tls`

- نمایش راهنما:

`cockpit-ws --help`
