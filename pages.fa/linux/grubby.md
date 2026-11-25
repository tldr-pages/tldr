# grubby

> ابزار پیکربندی بارگذارهای راه‌انداز `grub` و `zipl`.
> اطلاعات بیشتر: <https://manned.org/grubby.8>.

- افزودن آرگومان‌های راه‌اندازی هسته به همهٔ ورودی‌های منوی هسته:

`sudo grubby --update-kernel=ALL --args '{{quiet console=ttyS0}}'`

- حذف آرگومان‌های موجود از ورودی هستهٔ پیش‌فرض:

`sudo grubby --update-kernel=DEFAULT --remove-args {{quiet}}`

- فهرست کردن همهٔ ورودی‌های منوی هسته:

`sudo grubby --info=ALL`
