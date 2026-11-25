# fs_cli

> اتصال به سرور FreeSWITCH در حال اجرا و کنترل آن با رابط خط فرمان FreeSWITCH (کارخواه ESL).
> اطلاعات بیشتر: <https://developer.signalwire.com/freeswitch/FreeSWITCH-Explained/Client-and-Developer-Interfaces/1048948/>.

- اتصال به نمونهٔ محلی FreeSWITCH در یک نشست تعاملی:

`fs_cli`

- اتصال به سرور راه دور FreeSWITCH:

`fs_cli {{[-H|--host]}} {{host}} {{[-P|--port]}} {{port}} {{[-p|--password]}} {{password}}`

- اجرای یک دستور FreeSWITCH و خروج:

`fs_cli {{[-x|--execute]}} "{{command}}"`

- نمایش وضعیت سیستم FreeSWITCH:

`fs_cli {{[-x|--execute]}} "status"`

- بارگذاری مجدد پیکربندی XML مربوط به FreeSWITCH:

`fs_cli {{[-x|--execute]}} "reloadxml"`

- بررسی بارگذاری بودن یک ماژول:

`fs_cli {{[-x|--execute]}} "module_exists {{module_name}}"`

- نمایش تماس‌های فعال:

`fs_cli {{[-x|--execute]}} "show calls"`

- تلاش مجدد برای اتصال در صورت شکست:

`fs_cli {{[-r|--retry]}}`
