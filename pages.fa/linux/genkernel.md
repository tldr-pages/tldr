# genkernel

> ابزار جنتو لینوکس برای کامپایل و نصب هسته‌ها.
> اطلاعات بیشتر: <https://wiki.gentoo.org/wiki/Genkernel>.

- کامپایل و نصب خودکار یک هستهٔ عمومی:

`sudo genkernel all`

- ساخت و نصب فقط bzImage، initramfs، هسته یا ramdisk:

`sudo genkernel {{bzImage|initramfs|kernel|ramdisk}}`

- اعمال تغییرات در پیکربندی هسته پیش از کامپایل و نصب:

`sudo genkernel --menuconfig all`

- تولید هسته با نام دلخواه:

`sudo genkernel --kernname={{custom_name}} all`

- استفاده از منبع هسته خارج از دایرکتوری پیش‌فرض `/usr/src/linux`:

`sudo genkernel --kerneldir={{path/to/directory}} all`
