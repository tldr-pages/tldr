# microcom

> برنامهٔ ترمینال ساده برای دسترسی از کنسول به دستگاه‌های راه دور از طریق اتصال سریال، CAN یا telnet.
> اطلاعات بیشتر: <https://manned.org/microcom>.

- باز کردن پورت سریال با نرخ باد مشخص:

`microcom {{[-p|--port]}} {{/dev/ttyXYZ}} {{[-s|--speed]}} {{baud_rate}}`

- برقراری اتصال telnet به میزبان مشخص:

`microcom {{[-t|--telnet]}} {{hostname}}:{{port}}`
