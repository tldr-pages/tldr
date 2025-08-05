# phpquery

> Debian 기반 운영체제를 위한 PHP 확장 관리자.
> 더 많은 정보: <https://code.google.com/archive/p/phpquery/wikis/CommandLineInterface.wiki>.

- 사용 가능한 PHP 버전 나열:

`sudo phpquery -V`

- PHP 7.3에 대한 사용 가능한 SAPI 나열:

`sudo phpquery -v {{7.3}} -S`

- PHP 7.3의 cli SAPI에 대해 활성화된 확장 나열:

`sudo phpquery -v {{7.3}} -s {{cli}} -M`

- PHP 7.3의 apache2 SAPI에 대해 JSON 확장이 활성화되었는지 확인:

`sudo phpquery -v {{7.3}} -s {{apache2}} -m {{json}}`
