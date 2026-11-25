# kernel-install

> افزودن و حذف تصاویر هسته و initrd در `/boot`.
> اطلاعات بیشتر: <https://www.freedesktop.org/software/systemd/man/latest/kernel-install.html>.

- نمایش پیکربندی فعلی هسته که تنظیم یا به‌طور خودکار شناسایی شده است:

`kernel-install`

- نمایش پیکربندی تصویر هستهٔ مشخص:

`kernel-install inspect {{path/to/kernel_image}}`

- افزودن هسته به پارتیشن راه‌انداز:

`sudo kernel-install add {{kernel_version}} {{path/to/kernel_image}}`

- افزودن هسته و تصاویر initramfs به پارتیشن راه‌انداز:

`sudo kernel-install add {{kernel_version}} {{path/to/kernel_image}} {{path/to/initrd1 path/to/initrd2 ...}}`

- حذف هسته از پارتیشن راه‌انداز:

`sudo kernel-install remove {{kernel_version}}`
