# phpenmod

> A PHP-bővítmények engedélyezése Debian-alapú operációs rendszereken. További információ: <https://salsa.debian.org/php-team/php-defaults>.

- Engedélyezze a JSON kiterjesztést minden SAPI minden PHP-verzióhoz:

`sudo phpenmod {{json}}`

- Engedélyezze a JSON kiterjesztést a PHP 7.3-hoz a cli SAPI-val:

`sudo phpenmod -v {{7.3}} -s {{cli}} {{json}}`
