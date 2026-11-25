# mkswap

> آماده‌سازی فضای swap لینوکس روی دستگاه یا در فایل.
> توجه: `path/to/file` می‌تواند به فایل معمولی یا پارتیشن swap اشاره کند.
> اطلاعات بیشتر: <https://manned.org/mkswap>.

- آماده‌سازی فضای swap مشخص:

`sudo mkswap {{path/to/file}}`

- بررسی بلوک‌های خراب پارتیشن پیش از ایجاد فضای swap:

`sudo mkswap {{[-c|--check]}} {{path/to/file}}`

- تعیین برچسب برای پارتیشن (برای استفادهٔ `swapon` از برچسب):

`sudo mkswap {{[-L|--label]}} {{label}} {{/dev/sdXY}}`

- استفاده از UUID مشخص:

`sudo mkswap {{[-U|--uuid]}} {{clear|random|time|uuid_value}}`

- آماده‌سازی فایل swap (برای btrfs به‌جای آن `tldr btrfs filesystem` را ببینید):

`sudo mkswap {{[-s|--size]}} {{file_size}} {{[-F|--file]}} {{path/to/swapfile}}`
