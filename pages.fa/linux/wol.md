# wol

> کارخواه ارسال بسته‌های جادویی Wake-on-LAN.
> اطلاعات بیشتر: <https://sourceforge.net/projects/wake-on-lan/>.

- ارسال بستهٔ WoL به دستگاه:

`wol {{mac_address}}`

- ارسال بستهٔ WoL به دستگاهی در زیرشبکهٔ دیگر بر اساس IP آن:

`wol {{[-i|--ipaddr]}} {{ip_address}} {{mac_address}}`

- ارسال بستهٔ WoL به دستگاهی در زیرشبکهٔ دیگر بر اساس نام میزبان آن:

`wol {{[-h|--host]}} {{hostname}} {{mac_address}}`

- ارسال بستهٔ WoL به پورت مشخص میزبان:

`wol {{[-p|--port]}} {{port_number}} {{mac_address}}`

- خواندن آدرس‌های سخت‌افزاری، آدرس‌های IP یا نام میزبان، پورت‌های اختیاری و رمزهای عبور SecureON از فایل:

`wol {{[-f|--file]}} {{path/to/file}}`

- فعال کردن خروجی مفصل:

`wol {{[-v|--verbose]}} {{mac_address}}`
