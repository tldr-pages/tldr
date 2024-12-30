# 打开

> 使用默认应用程序打开文件、目录和 URI。
> 该命令可以通过 fish 在没有内置 `open` 命令的操作系统上使用（例如 Haiku 和 macOS）。
> 更多信息：<https://fishshell.com/docs/current/cmds/open.html>。

- 使用关联的应用程序打开文件：

`open {{path/to/file.ext}}`

- 使用关联的应用程序打开当前目录中所有给定扩展名的文件：

`open {{*.ext}}`

- 使用默认文件管理器打开目录：

`open {{path/to/directory}}`

- 使用默认网页浏览器打开网站：

`open {{https://example.com}}`

- 使用可以处理它的默认应用程序打开特定 URI：

`open {{tel:123}}`