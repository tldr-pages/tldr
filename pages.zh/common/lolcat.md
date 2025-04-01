# lolcat

> 为所有通过 `cat` 命令输出到控制台的内容添加彩虹效果。
> 更多信息：<https://github.com/busyloop/lolcat>.

- 以彩虹色输出文件内容到控制台：

`lolcat {{path/to/file}}`

- 将文本生成命令的结果以彩虹色输出到控制台：

`{{fortune}} | lolcat`

- 以动画彩虹色输出文件内容到控制台：

`lolcat -a {{path/to/file}}`

- 以24位（真彩色）彩虹色输出文件内容到控制台：

`lolcat -t {{path/to/file}}`