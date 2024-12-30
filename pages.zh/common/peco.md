# peco

> 交互式过滤工具。
> 更多信息：<https://github.com/peco/peco>。

- 在指定目录下的所有文件中启动 `peco`：

`find {{path/to/directory}} -type f | peco`

- 启动 `peco` 查看正在运行的进程：

`ps aux | peco`

- 使用指定查询启动 `peco`：

`peco --query "{{query}}"`