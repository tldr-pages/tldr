# systemd-detect-virt

> تشخیص اجرا در محیط مجازی.
> اطلاعات بیشتر: <https://www.freedesktop.org/software/systemd/man/latest/systemd-detect-virt.html>.

- فهرست کردن فناوری‌های مجازی‌سازی قابل تشخیص:

`systemd-detect-virt --list`

- تشخیص مجازی‌سازی، چاپ نتیجه و بازگرداندن کد صفر هنگام اجرا در ماشین مجازی یا کانتینر و کد غیرصفر در غیر این صورت:

`systemd-detect-virt`

- بررسی بی‌صدا بدون چاپ:

`systemd-detect-virt {{[-q|--quiet]}}`

- تشخیص فقط مجازی‌سازی کانتینر:

`systemd-detect-virt {{[-c|--container]}}`

- تشخیص فقط مجازی‌سازی سخت‌افزاری:

`systemd-detect-virt {{[-v|--vm]}}`

- تشخیص قرار داشتن در محیط `chroot`:

`systemd-detect-virt {{[-r|--chroot]}}`
