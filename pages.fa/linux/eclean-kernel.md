# eclean-kernel

> حذف هسته‌های قدیمی در جنتو.
> اطلاعات بیشتر: <https://wiki.gentoo.org/wiki/Kernel/Removal#Using_eclean-kernel>.

- فهرست کردن همهٔ فایل‌های هسته:

`sudo eclean-kernel {{[-l|--list-kernels]}}`

- حذف همهٔ هسته‌ها به‌جز دو هستهٔ جدیدتر:

`sudo eclean-kernel {{[-n|--num]}} 2`

- حذف همهٔ هسته‌ها به‌جز دو هستهٔ جدیدتر و درخواست تأیید پیش از حذف:

`sudo eclean-kernel {{[-a|--all]}} {{[-n|--num]}} 2`
