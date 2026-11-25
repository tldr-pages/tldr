# pyrit

> ابزار شکستن WPA/WPA2 با استفاده از توان محاسباتی.
> اطلاعات بیشتر: <https://manned.org/pyrit>.

- نمایش سرعت شکستن سیستم:

`pyrit benchmark`

- فهرست کردن هسته‌های موجود:

`pyrit list_cores`

- تنظیم ESSID:

`pyrit -e "{{extended_ssid}}" create_essid`

- خواندن و تحلیل فایل ضبط بستهٔ مشخص:

`pyrit -r {{path/to/file}}.{{cap|pcap}} analyze`

- خواندن و وارد کردن رمزهای عبور به پایگاه دادهٔ فعلی:

`pyrit -i {{path/to/file}} {{import_unique_passwords|unique_passwords|import_passwords}}`

- صادر کردن رمزهای عبور از پایگاه داده به فایل مشخص:

`pyrit -o {{path/to/file}} export_passwords`

- تبدیل رمزهای عبور با کلیدهای اصلی Pired:

`pyrit batch`

- خواندن فایل ضبط و شکستن رمز عبور:

`pyrit -r {{path/to/file}} attack_db`
