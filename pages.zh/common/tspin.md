# tspin

> 一个基于 `less` 分页器的日志文件高亮工具，基本行为类似于任何分页器。
> 更多信息：<https://github.com/bensadeh/tailspin>。

- 从文件读取并在 `less` 中查看：

`tspin {{path/to/application.log}}`

- 从另一个命令读取并输出到标准输出：

`journalctl -b --follow | tspin`

- 从文件读取并输出到标准输出：

`tspin {{path/to/application.log}} --print`

- 从 `stdin` 读取并输出到标准输出：

`echo "2021-01-01 12:00:00 [INFO] This is a log message" | tspin`