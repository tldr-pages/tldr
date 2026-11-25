# phpdismod

> غیرفعال کردن افزونه‌های PHP در سیستم‌عامل‌های مبتنی بر Debian.
> اطلاعات بیشتر: <https://salsa.debian.org/php-team/php-defaults>.

- غیرفعال کردن افزونهٔ JSON برای هر SAPI از هر نسخهٔ PHP:

`sudo phpdismod {{json}}`

- غیرفعال کردن افزونهٔ JSON برای PHP 7.3 با SAPI نوع cli:

`sudo phpdismod -v {{7.3}} -s {{cli}} {{json}}`
