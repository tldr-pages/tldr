# lp

> 打印文件。
> 更多信息：<https://manned.org/lp>。

- 将命令的输出打印到默认打印机（参见 `lpstat` 命令）：

`echo "test" | lp`

- 将文件打印到默认打印机：

`lp {{path/to/filename}}`

- 将文件打印到指定打印机（参见 `lpstat` 命令）：

`lp -d {{printer_name}} {{path/to/filename}}`

- 将文件打印 `n` 份到默认打印机：

`lp -n {{n}} {{path/to/filename}}`

- 仅打印特定页面到默认打印机（打印第 1、3-5 和 16 页）：

`lp -P 1,3-5,16 {{path/to/filename}}`

- 恢复打印作业：

`lp -i {{job_id}} -H resume`