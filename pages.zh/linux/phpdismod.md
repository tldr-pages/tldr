# phpdismod

> 在基于 Debian 的操作系统上禁用 PHP 扩展。
> 更多信息：<https://salsa.debian.org/php-team/php-defaults>.

- 禁用所有 PHP 版本的所有 SAPI 的 JSON 扩展：

`sudo phpdismod {{json}}`

- 禁用 PHP 7.3 的 cli SAPI 的 JSON 扩展：

`sudo phpdismod -v {{7.3}} -s {{cli}} {{json}}`
