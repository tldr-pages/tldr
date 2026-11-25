# update-ca-certificates

> به‌روزرسانی مجموعهٔ گواهی‌های CA و تولید مجدد `/etc/ssl/certs`.
> اطلاعات بیشتر: <https://manned.org/update-ca-certificates>.

- به‌روزرسانی گواهی‌ها:

`sudo update-ca-certificates`

- به‌روزرسانی گواهی‌ها در حالت مفصل:

`sudo update-ca-certificates {{[-v|--verbose]}}`

- انجام به‌روزرسانی تازه (حذف همهٔ پیوندهای نمادین و تولید مجدد):

`sudo update-ca-certificates {{[-f|--fresh]}}`

- افزودن گواهی دلخواه (ابتدا آن را کپی و سپس به‌روزرسانی کنید):

`sudo cp {{path/to/certificate.crt}} /usr/local/share/ca-certificates/ && sudo update-ca-certificates`
