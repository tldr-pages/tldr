# phpdismod

> Disable PHP extensions on Debian-based OSes.
> More information: https://linuxcommandlibrary.com/man/phpdismod

- Disable the JSON extension for every SAPI of every PHP version:

`sudo phpdismod {{json}}`

- Disable the JSON extension for PHP 7.3 with the cli SAPI:

`sudo phpdismod -v {{7.3}} -s {{cli}} {{json}}`
