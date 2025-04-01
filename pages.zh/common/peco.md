# peco

> 交互式过滤工具。
> 更多信息：<https://github.com/peco/peco>.

- 在指定目录中的所有文件上启动 `peco`：

`find {{path/to/directory}} -type f | peco`

- 为正在运行的进程启动 `peco`：

`ps aux | peco`

- 带指定查询启动 `peco`：

`peco --query "{{query}}"`
