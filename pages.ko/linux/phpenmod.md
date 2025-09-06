# phpenmod

> Debian 계열 OS에서 PHP 확장을 활성화.
> 더 많은 정보: <https://salsa.debian.org/php-team/php-defaults>.

- 모든 PHP 버전의 모든 SAPI에 대해 JSON 확장 활성화:

`sudo phpenmod {{json}}`

- PHP 7.3의 cli SAPI에 대해 JSON 확장 활성화:

`sudo phpenmod -v {{7.3}} -s {{cli}} {{json}}`
