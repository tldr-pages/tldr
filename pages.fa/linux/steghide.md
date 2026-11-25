# steghide

> ابزار پنهان‌نگاری برای قالب‌های JPEG، BMP، WAV و AU.
> اطلاعات بیشتر: <https://manned.org/steghide>.

- جاسازی داده در PNG با درخواست عبارت عبور:

`steghide embed {{[-cf|--coverfile]}} {{path/to/image.png}} {{[-ef|--embedfile]}} {{path/to/data.txt}}`

- استخراج داده از فایل صوتی WAV:

`steghide extract {{[-sf|--stegofile]}} {{path/to/sound.wav}}`

- نمایش اطلاعات فایل و تلاش برای شناسایی فایل جاسازی‌شده:

`steghide info {{path/to/file.jpg}}`

- جاسازی داده در تصویر JPEG با حداکثر فشرده‌سازی:

`steghide embed {{[-cf|--coverfile]}} {{path/to/image.jpg}} {{[-ef|--embedfile]}} {{path/to/data.txt}} {{[-z|--compress]}} {{9}}`

- دریافت فهرست الگوریتم‌ها و حالت‌های رمزگذاری پشتیبانی‌شده:

`steghide encinfo`

- جاسازی دادهٔ رمزگذاری‌شده در تصویر JPEG، مثلاً با Blowfish در حالت CBC:

`steghide embed {{[-cf|--coverfile]}} {{path/to/image.jpg}} {{[-ef|--embedfile]}} {{path/to/data.txt}} {{[-e|--encryption]}} {{blowfish|...}} {{cbc|...}}`
