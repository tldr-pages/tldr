# phpdismod

> 在基于Debian的操作系统上禁用PHP扩展。
> 更多信息：<https://salsa.debian.org/php-team/php-defaults>。

- 对于每个PHP版本的每个SAPI禁用JSON扩展：

`sudo phpdismod {{json}}`

- 对PHP 7.3的cli SAPI禁用JSON扩展：

`sudo phpdismod -v {{7.3}} -s {{cli}} {{json}}`