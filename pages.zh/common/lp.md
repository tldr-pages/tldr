# lp

> 打印文件。
> 更多信息：<https://manned.org/lp>。

- 将命令的输出打印到默认打印机（请参见 `lpstat` 命令）：

`echo "test" | lp`

- 将文件打印到默认打印机：

`lp {{path/to/filename}}`

- 将文件打印到指定打印机（请参见 `lpstat` 命令）：

`lp -d {{printer_name}} {{path/to/filename}}`

- 将文件的 N 份打印到默认打印机（将 N 替换为所需的份数）：

`lp -n {{N}} {{path/to/filename}}`

- 仅将特定页面打印到默认打印机（打印页面 1、3-5 和 16）：

`lp -P 1,3-5,16 {{path/to/filename}}`

- 恢复打印作业：

`lp -i {{job_id}} -H resume`