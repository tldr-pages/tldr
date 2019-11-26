# phpenmod

> Enable PHP extensions on Debian-based OSes.

- Enable the json extension for every SAPI of every PHP version:

`sudo phpenmod {{json}}`

- Enable the json extension for PHP 7.3 with the cli SAPI:

`sudo phpenmod -v {{7.3}} -s {{cli}} {{json}}`
