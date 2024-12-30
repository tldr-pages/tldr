# wp

> 管理 WordPress 实例的官方命令行界面。
> 更多信息：<https://wp-cli.org/>。

- 打印关于操作系统、shell、PHP 和 WP-CLI (`wp`) 安装的信息：

`wp --info`

- 更新 WP-CLI：

`wp cli update`

- 下载一个全新的 WordPress 安装到当前目录， 可选地指定语言环境：

`wp core download --locale={{locale}}`

- 创建基本的 `wpconfig` 文件（假设数据库在 `localhost` 上）：

`wp config create --dbname={{dbname}} --dbuser={{dbuser}} --dbpass={{dbpass}}`

- 安装并激活一个 WordPress 插件：

`wp plugin install {{plugin}} --activate`

- 替换数据库中字符串的所有实例：

`wp search-replace {{old_string}} {{new_string}}`

- 导入 WordPress 扩展 RSS (WXR) 文件的内容：

`wp import {{path/to/file.xml}}`