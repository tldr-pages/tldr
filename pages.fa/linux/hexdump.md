# hexdump

> چاپ محتویات در قالب ASCII، ده‌دهی، شانزده‌شانزدهی یا هشت‌هشتی.
> همچنین : `hexyl`, `od`, `xxd`.
> اطلاعات بیشتر: <https://manned.org/hexdump>.

- چاپ نمایش شانزده‌شانزدهی فایل و جایگزینی خط‌های تکراری با «*»:

`hexdump {{path/to/file}}`

- نمایش آفست ورودی به‌صورت شانزده‌شانزدهی و نمایش ASCII آن در دو ستون:

`hexdump {{[-C|--canonical]}} {{path/to/file}}`

- نمایش فایل به‌صورت شانزده‌شانزدهی با تفسیر فقط n بایت از ورودی:

`hexdump {{[-C|--canonical]}} {{[-n|--length]}} {{number_of_bytes}} {{path/to/file}}`

- جایگزین نکردن خط‌های تکراری با «*»:

`hexdump {{[-v|--no-squeezing]}} {{path/to/file}}`
