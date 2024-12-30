# pickle

> 一个基于 Composer 的 PHP 扩展安装器。
> 更多信息：<https://github.com/FriendsOfPHP/pickle>。

- 安装特定的 PHP 扩展：

`pickle install {{extension_name}}`

- 将现有的 PECL 扩展配置转换为 Pickle 配置文件：

`pickle convert {{path/to/directory}}`

- 验证一个 PECL 扩展：

`pickle validate {{path/to/directory}}`

- 打包一个 PECL 扩展以供发布：

`pickle release {{path/to/directory}}`