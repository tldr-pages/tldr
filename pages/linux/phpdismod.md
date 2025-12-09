# phpdismod

> Disable PHP extensions on Debian-based OSes.
> More information: <https://salsa.debian.org/php-team/php-defaults>.

- Disable the JSON extension for every SAPI of every PHP version:

`sudo phpdismod {{json}}`

- Disable the JSON extension for PHP 7.3 with the cli SAPI:

`sudo phpdismod -v {{7.3}} -s {{cli}} {{json}}`
