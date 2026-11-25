# torsocks

> مسیریابی ترافیک هر برنامه از طریق شبکهٔ Tor.
> توجه: `torsocks` به‌طور پیش‌فرض فرض می‌کند باید به پراکسی SOCKS مربوط به Tor در 127.0.0.1:9050 متصل شود که پیش‌فرض سرویس Tor است.
> اطلاعات بیشتر: <https://manned.org/torsocks>.

- اجرای دستور با استفاده از Tor:

`torsocks {{command}}`

- فعال یا غیرفعال کردن Tor در این پوسته:

`. torsocks {{on|off}}`

- ایجاد پوستهٔ جدید مجهز به Tor:

`torsocks --shell`

- بررسی فعال بودن Tor در پوستهٔ فعلی (در صورت غیرفعال بودن مقدار `$LD_PRELOAD` خالی است):

`torsocks show`

- جداسازی ترافیک از طریق مدار متفاوت Tor برای بهبود ناشناسی:

`torsocks {{[-i|--isolate]}} {{curl https://check.torproject.org/api/ip}}`

- اتصال به پراکسی Tor در آدرس و پورت مشخص:

`torsocks {{[-a|--address]}} {{ip_address}} {{[-P|--port]}} {{port}} {{command}}`
