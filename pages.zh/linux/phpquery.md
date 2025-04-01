# phpquery

> 面向 Debian 系操作系统的 PHP 扩展管理器。
> 更多信息：<https://helpmanual.io/help/phpquery/>.

- 列出可用的 PHP 版本：

`sudo phpquery -V`

- 列出 PHP 7.3 的可用 SAPI：

`sudo phpquery -v {{7.3}} -S`

- 列出 PHP 7.3（使用 cli SAPI）的已启用扩展：

`sudo phpquery -v {{7.3}} -s {{cli}} -M`

- 检查 PHP 7.3（使用 apache2 SAPI）是否启用了 JSON 扩展：

`sudo phpquery -v {{7.3}} -s {{apache2}} -m {{json}}`