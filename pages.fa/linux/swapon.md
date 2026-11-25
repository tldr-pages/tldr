# swapon

> فعال کردن دستگاه‌ها و فایل‌ها برای swap.
> توجه: `path/to/file` می‌تواند به فایل معمولی یا پارتیشن swap اشاره کند.
> اطلاعات بیشتر: <https://manned.org/swapon.8>.

- نمایش اطلاعات swap:

`swapon`

- فعال کردن فضای swap مشخص:

`sudo swapon {{path/to/file}}`

- فعال کردن همهٔ فضاهای swap مشخص‌شده در `/etc/fstab` به‌جز موارد دارای گزینهٔ `noauto`:

`sudo swapon {{[-a|--all]}}`

- فعال کردن پارتیشن swap با برچسب آن:

`sudo swapon -L {{label}}`
