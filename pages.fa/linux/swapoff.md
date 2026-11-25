# swapoff

> غیرفعال کردن دستگاه‌ها و فایل‌ها برای swap.
> توجه: `path/to/file` می‌تواند به فایل معمولی یا پارتیشن swap اشاره کند.
> اطلاعات بیشتر: <https://manned.org/swapoff.8>.

- غیرفعال کردن فضای swap مشخص:

`sudo swapoff {{path/to/file}}`

- غیرفعال کردن همهٔ فضاهای swap در `/proc/swaps`:

`sudo swapoff {{[-a|--all]}}`

- غیرفعال کردن پارتیشن swap با برچسب آن:

`sudo swapoff -L {{label}}`
