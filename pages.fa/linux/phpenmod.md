# phpenmod

> فعال کردن افزونه‌های PHP در سیستم‌عامل‌های مبتنی بر Debian.
> اطلاعات بیشتر: <https://salsa.debian.org/php-team/php-defaults>.

- فعال کردن افزونهٔ JSON برای هر SAPI از هر نسخهٔ PHP:

`sudo phpenmod {{json}}`

- فعال کردن افزونهٔ JSON برای PHP 7.3 با SAPI نوع cli:

`sudo phpenmod -v {{7.3}} -s {{cli}} {{json}}`
