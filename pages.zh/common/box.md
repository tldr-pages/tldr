# box

> 一个用于构建和管理 Phar 的 PHP 应用程序。
> 更多信息：<https://github.com/box-project/box>。

- 编译一个新的 Phar 文件：

`box compile`

- 使用特定的 [c]onfiguration 文件编译一个新的 Phar 文件：

`box compile -c {{path/to/config}}`

- 显示关于 PHAR PHP 扩展的信息：

`box info`

- 显示关于特定 Phar 文件的信息：

`box info {{path/to/phar_file}}`

- 验证工作目录中找到的第一个配置文件：

`box validate`

- 验证特定 Phar 文件的签名：

`box verify {{path/to/phar_file}}`

- 显示帮助信息：

`box help`