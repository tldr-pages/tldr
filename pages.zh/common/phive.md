# phive

> Phar 安装和验证环境，用于安全的 PHP 应用程序部署。
> 更多信息：<https://phar.io>。

- 显示可用别名 Phar 的列表：

`phive list`

- 将指定的 Phar 安装到本地目录：

`phive install {{alias|url}}`

- 将指定的 Phar 全局安装：

`phive install {{alias|url}} --global`

- 将指定的 Phar 安装到目标目录：

`phive install {{alias|url}} --target {{path/to/directory}}`

- 更新所有 Phar 文件到最新版本：

`phive update`

- 移除指定的 Phar 文件：

`phive remove {{alias|url}}`

- 移除未使用的 Phar 文件：

`phive purge`

- 列出所有可用命令：

`phive help`