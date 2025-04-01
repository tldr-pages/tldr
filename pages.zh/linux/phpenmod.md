# phpenmod

> 在基于 Debian 的操作系统上启用 PHP 扩展。
> 更多信息：<https://salsa.debian.org/php-team/php-defaults>.

- 为所有 PHP 版本的每个 SAPI 启用 JSON 扩展：

`sudo phpenmod {{json}}`

- 为 PHP 7.3 的 cli SAPI 启用 JSON 扩展：

`sudo phpenmod -v {{7.3}} -s {{cli}} {{json}}`