# systemd-machine-id-setup

> مقداردهی اولیهٔ شناسهٔ دستگاه در `/etc/machine-id` هنگام نصب با شناسهٔ ازپیش‌تأمین‌شده یا تصادفی.
> توجه: این دستورها به دسترسی بالا نیاز دارند، پس همواره با `sudo` اجرا کنید.
> اطلاعات بیشتر: <https://www.freedesktop.org/software/systemd/man/latest/systemd-machine-id-setup.html>.

- چاپ شناسهٔ دستگاه تولید یا ثبت‌شده:

`systemd-machine-id-setup --print`

- تعیین سیاست تصویر:

`systemd-machine-id-setup --image-policy {{your_policy}}`

- نمایش خروجی به‌صورت JSON:

`sudo systemd-machine-id-setup --json pretty`

- عمل روی تصویر دیسک به‌جای درخت دایرکتوری:

`systemd-machine-id-setup --image /{{path/to/image}}`
