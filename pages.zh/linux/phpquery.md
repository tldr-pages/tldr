# phpquery

> Debian基础操作系统的PHP扩展管理器。
> 更多信息：<https://helpmanual.io/help/phpquery/>。

- 列出可用的PHP版本：

`sudo phpquery -V`

- 列出PHP 7.3的可用SAPI：

`sudo phpquery -v {{7.3}} -S`

- 列出PHP 7.3在cli SAPI下启用的扩展：

`sudo phpquery -v {{7.3}} -s {{cli}} -M`

- 检查PHP 7.3在apache2 SAPI下是否启用了JSON扩展：

`sudo phpquery -v {{7.3}} -s {{apache2}} -m {{json}}`