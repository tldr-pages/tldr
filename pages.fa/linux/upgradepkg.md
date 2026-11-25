# upgradepkg

> ارتقای بسته‌های Slackware با جایگزینی بسته‌های موجود با نسخه‌های جدید.
> همچنین : `installpkg`, `removepkg`, `makepkg`, `pkgtool`.
> اطلاعات بیشتر: <https://slackware.nl/slackware/slackware64-current/source/a/pkgtools/manpages/upgradepkg.8>.

- ارتقای بسته:

`sudo upgradepkg {{path/to/package.tgz}}`

- ارتقای بسته و نصب آن در صورت نبود:

`sudo upgradepkg --install-new {{path/to/package.tgz}}`

- نصب مجدد بسته (حتی اگر همان نسخه از قبل نصب باشد):

`sudo upgradepkg --reinstall {{path/to/package.tgz}}`

- شبیه‌سازی ارتقا و نمایش نتیجهٔ احتمالی:

`upgradepkg --dry-run {{path/to/package.tgz}}`

- ارتقای بسته و نمایش پیشرفت مفصل:

`sudo upgradepkg --verbose {{path/to/package.tgz}}`
