# getArch.py

> 确定远程 Windows 系统的 OS 架构（x86 或 x64）。
> 是 Impacket 套件的一部分。
> 更多信息：<https://github.com/fortra/impacket>.

- 检查单个目标系统的架构：

`getArch.py -target {{target}}`

- 从文件中检查多个目标的架构（每行一个目标）：

`getArch.py -targets {{path/to/targets_file}}`

- 设置自定义套接字超时时间（默认为 2 秒）：

`getArch.py -target {{target}} -timeout {{seconds}}`

- 启用调试模式以获取详细输出：

`getArch.py -target {{target}} -debug`
