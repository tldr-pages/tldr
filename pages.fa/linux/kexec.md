# kexec

> راه‌اندازی مجدد مستقیم به هستهٔ جدید.
> اطلاعات بیشتر: <https://manned.org/kexec>.

- بارگذاری هستهٔ جدید:

`kexec {{[-l|--load]}} {{path/to/kernel}} --initrd={{path/to/initrd}} --command-line={{arguments}}`

- بارگذاری هستهٔ جدید با پارامترهای راه‌اندازی فعلی:

`kexec {{[-l|--load]}} {{path/to/kernel}} --initrd={{path/to/initrd}} --reuse-cmdline`

- اجرای هسته‌ای که اکنون بارگذاری شده است:

`kexec {{[-e|--exec]}}`

- خارج کردن هستهٔ مقصد فعلی kexec از حافظه:

`kexec {{[-u|--unload]}}`
