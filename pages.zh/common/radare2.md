# radare2

> 一套反向工程工具。
> 更多信息：<https://www.radare.org/r/docs.html>。

- 以写入模式打开文件，而不解析文件格式头：

`radare2 -nw {{path/to/binary}}`

- 调试程序：

`radare2 -d {{path/to/binary}}`

- 在进入交互式 CLI 之前运行脚本：

`radare2 -i {{path/to/script.r2}} {{path/to/binary}}`

- 在交互式 CLI 中显示任何命令的帮助文本：

`> {{radare2_command}}?`

- 从交互式 CLI 中运行 shell 命令：

`> !{{shell_command}}`

- 将当前块的原始字节转储到文件中：

`> pr > {{path/to/file.bin}}`
