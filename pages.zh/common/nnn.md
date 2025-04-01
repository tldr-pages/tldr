# nnn

> 交互式终端文件管理器和磁盘使用情况分析器。
> 更多信息：<https://github.com/jarun/nnn/wiki/Usage#program-options>.

- 打开当前目录（或作为第一个参数指定一个目录）：

`nnn`

- 以详细模式启动：

`nnn -d`

- 显示隐藏文件：

`nnn -H`

- 打开已有的书签（在 `NNN_BMS` 环境变量中定义）：

`nnn -b {{bookmark_name}}`

- 按 [a] 显示的磁盘使用情况 / [d] 磁盘使用情况 / [e] 扩展名 / [r] 逆序 / [s] 大小 / [t] 时间 / [v] 版本排序文件：

`nnn -T {{a|d|e|r|s|t|v}}`

- 打开选定的文件。选择文件后，按 `<o>`，然后输入要使用的程序打开文件：

`nnn -o`
