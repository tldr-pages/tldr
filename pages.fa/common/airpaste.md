# airpaste

> اشتراک گذاری پیام و فایل از طریق شبکه مشترک با استفاده از mDNS.
> اطلاعات بیشتر: <https://github.com/mafintosh/airpaste>.

- منتظر پیام می ماند و هنگام دریافت آن را نشان می دهد:

`airpaste`

- ارسال متن:

`echo {{text}} | airpaste`

- ارسال فایل:

`airpaste < {{path/to/file}}`

- دریافت فایل:

`airpaste > {{path/to/file}}`

- ساخت یا ورود به یک کانال:

`airpaste {{channel_name}}`
