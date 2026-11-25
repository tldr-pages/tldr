# phpquery

> مدیر افزونه‌های PHP برای سیستم‌عامل‌های مبتنی بر Debian.
> اطلاعات بیشتر: <https://code.google.com/archive/p/phpquery/wikis/CommandLineInterface.wiki>.

- فهرست کردن نسخه‌های موجود PHP:

`sudo phpquery -V`

- فهرست کردن SAPIهای موجود برای PHP 7.3:

`sudo phpquery -v {{7.3}} -S`

- فهرست کردن افزونه‌های فعال برای PHP 7.3 با SAPI نوع cli:

`sudo phpquery -v {{7.3}} -s {{cli}} -M`

- بررسی فعال بودن افزونهٔ JSON برای PHP 7.3 با SAPI نوع apache2:

`sudo phpquery -v {{7.3}} -s {{apache2}} -m {{json}}`
