# nixos-rebuild

> پیکربندی مجدد دستگاه NixOS.
> اطلاعات بیشتر: <https://nixos.org/nixos/manual/#sec-changing-config>.

- ساخت و تغییر به پیکربندی جدید و قرار دادن آن به‌عنوان پیش‌فرض راه‌اندازی:

`sudo nixos-rebuild switch`

- ساخت و تغییر به پیکربندی جدید، قرار دادن آن به‌عنوان پیش‌فرض راه‌اندازی و نام‌گذاری ورودی راه‌اندازی:

`sudo nixos-rebuild switch {{[-p|--profile-name]}} {{name}}`

- ساخت و تغییر به پیکربندی جدید، قرار دادن آن به‌عنوان پیش‌فرض راه‌اندازی و نصب به‌روزرسانی‌ها:

`sudo nixos-rebuild switch --upgrade`

- بازگرداندن تغییرات پیکربندی و تغییر به نسل قبلی:

`sudo nixos-rebuild switch --rollback`

- ساخت پیکربندی جدید و قرار دادن آن به‌عنوان پیش‌فرض راه‌اندازی بدون تغییر به آن:

`sudo nixos-rebuild boot`

- ساخت و فعال کردن پیکربندی جدید بدون ایجاد ورودی راه‌اندازی (برای آزمون):

`sudo nixos-rebuild test`

- ساخت پیکربندی و باز کردن آن در ماشین مجازی:

`sudo nixos-rebuild build-vm`

- فهرست کردن نسل‌های موجود مشابه منوی راه‌انداز:

`nixos-rebuild list-generations`
