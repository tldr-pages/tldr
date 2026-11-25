# dnf download

> دانلود بسته‌های RPM از مخازن DNF.
> به‌صورت پیش‌فرض بخشی از `dnf` نیست، اما از طریق `dnf-plugins-core` پشتیبانی می‌شود.
> اطلاعات بیشتر: <https://dnf-plugins-core.readthedocs.io/en/latest/download.html>.

- دانلود آخرین نسخهٔ یک بسته در دایرکتوری فعلی:

`dnf download {{package}}`

- دانلود یک بسته در دایرکتوری مشخص (دایرکتوری باید وجود داشته باشد):

`dnf download {{package}} --destdir {{path/to/directory}}`

- چاپ URL دانلود بستهٔ RPM:

`dnf download --url {{package}}`
