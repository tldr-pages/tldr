# wp

> 官方命令行接口，用于管理 WordPress 实例。
> 更多信息：<https://wp-cli.org/>.

- 打印有关操作系统、shell、PHP 和 WP-CLI (`wp`) 安装的信息：

`wp --info`

- 更新 WP-CLI：

`wp cli update`

- 在当前目录下载一个全新的 WordPress 安装包，可选指定语言区域：

`wp core download --locale={{locale}}`

- 创建基本的 `wpconfig` 文件（假设数据库位于 `localhost`）：

`wp config create --dbname={{dbname}} --dbuser={{dbuser}} --dbpass={{dbpass}}`

- 安装并激活 WordPress 插件：

`wp plugin install {{plugin}} --activate`

- 替换数据库中所有出现的字符串：

`wp search-replace {{old_string}} {{new_string}}`

- 导入 WordPress 扩展 RSS (WXR) 文件的内容：

`wp import {{path/to/file.xml}}`
