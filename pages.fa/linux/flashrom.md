# flashrom

> خواندن، نوشتن، اعتبارسنجی و پاک کردن تراشه‌های فلش.
> اطلاعات بیشتر: <https://manned.org/flashrom>.

- شناسایی تراشه و اطمینان از صحت سیم‌کشی:

`flashrom {{[-p|--programmer]}} {{programmer}}`

- خواندن فلش و ذخیرهٔ آن در فایل:

`flashrom {{[-p|--programmer]}} {{programmer}} {{[-r|--read]}} {{path/to/file}}`

- نوشتن یک فایل روی فلش:

`flashrom {{[-p|--programmer]}} {{programmer}} {{[-w|--write]}} {{path/to/file}}`

- اعتبارسنجی محتوای فلش در برابر فایل:

`flashrom {{[-p|--programmer]}} {{programmer}} {{[-v|--verify]}} {{path/to/file}}`

- شناسایی تراشه با Raspberry Pi:

`flashrom {{[-p|--programmer]}} {{linux_spi:dev=/dev/spidev0.0}}`
