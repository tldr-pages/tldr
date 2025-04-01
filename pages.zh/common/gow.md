# gow

> 监视 Go 文件并在文件更改时重新启动应用程序。
> 更多信息：<https://github.com/mitranim/gow>。

- 启动并监视当前目录：

`gow run .`

- 使用指定的参数启动应用程序：

`gow run . {{argument1 argument2 ...}}`

- 以详细模式监视子目录：

`gow -v -w={{path/to/directory1,path/to/directory2,...}} run .`

- 监视指定的文件扩展名：

`gow -e={{go,html}} run .`

- 显示帮助信息：

`gow -h`