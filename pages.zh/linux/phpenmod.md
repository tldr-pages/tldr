# phpenmod

> 在基于Debian的操作系统上启用PHP扩展。
> 更多信息：<https://salsa.debian.org/php-team/php-defaults>。

- 为每个PHP版本的每个SAPI启用JSON扩展：

`sudo phpenmod {{json}}`

- 为PHP 7.3的cli SAPI启用JSON扩展：

`sudo phpenmod -v {{7.3}} -s {{cli}} {{json}}`