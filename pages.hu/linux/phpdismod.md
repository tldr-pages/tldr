# phpdismod

> A PHP-bővítmények letiltása Debian-alapú operációs rendszereken. További információ: <https://salsa.debian.org/php-team/php-defaults>.

- Tiltja le a JSON kiterjesztést minden SAPI minden PHP verziójánál:

`sudo phpdismod {{json}}`

- Tiltsa le a JSON kiterjesztést a PHP 7.3 esetében a cli SAPI-val:

`sudo phpdismod -v {{7.3}} -s {{cli}} {{json}}`
