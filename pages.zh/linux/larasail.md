# larasail

> 在 Digital Ocean 服务器上管理 Laravel。
> 更多信息：<https://github.com/thedevdojo/larasail>。

- 使用默认 PHP 版本设置带有 Laravel 依赖的服务器：

`larasail setup`

- 使用特定 PHP 版本设置带有 Laravel 依赖的服务器：

`larasail setup {{php71}}`

- 添加一个新的 Laravel 网站：

`larasail host {{domain}} {{path/to/site_directory}}`

- 获取 Larasail 用户密码：

`larasail pass`

- 获取 Larasail MySQL 密码：

`larasail mysqlpass`