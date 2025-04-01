# phive

> 用于安全 PHP 应用部署的 Phar 安装和验证环境。
> 更多信息：<https://phar.io>。

- 显示可用的别名 Phar 列表：

`phive list`

- 安装指定的 Phar 到本地目录：

`phive install {{alias|url}}`

- 全局安装指定的 Phar：

`phive install {{alias|url}} --global`

- 安装指定的 Phar 到目标目录：

`phive install {{alias|url}} --target {{path/to/directory}}`

- 将所有 Phar 文件更新到最新版本：

`phive update`

- 移除指定的 Phar 文件：

`phive remove {{alias|url}}`

- 移除未使用的 Phar 文件：

`phive purge`

- 列出所有可用命令：

`phive help`