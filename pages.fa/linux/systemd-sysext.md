# systemd-sysext

> فعال یا غیرفعال کردن تصاویر افزونهٔ سیستم.
> اطلاعات بیشتر: <https://www.freedesktop.org/software/systemd/man/latest/systemd-sysext.html>.

- فهرست کردن تصاویر افزونهٔ نصب‌شده:

`systemd-sysext list`

- ادغام تصاویر افزونهٔ سیستم در `/usr/` و `/opt/`:

`systemd-sysext merge`

- بررسی وضعیت فعلی ادغام:

`systemd-sysext`

- جداسازی همهٔ تصاویر افزونهٔ سیستم نصب‌شده از `/usr/` و `/opt/`:

`systemd-sysext unmerge`

- تازه‌سازی تصاویر افزونهٔ سیستم (ترکیبی از `unmerge` و `merge`):

`systemd-sysext refresh`
