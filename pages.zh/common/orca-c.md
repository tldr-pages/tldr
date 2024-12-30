# orca-c

> ORCA实时编程环境的C语言移植版本。
> ORCA是一种用于创建程序序列器的晦涩编程语言。
> 更多信息：<https://github.com/hundredrabbits/Orca-c>。

- 使用空工作区启动ORCA：

`orca-c`

- 启动ORCA并打开特定文件：

`orca-c {{path/to/file.orca}}`

- 启动ORCA并设置特定的节拍（默认为120）：

`orca-c --bpm {{beats_per_minute}}`

- 启动ORCA并设置网格的大小：

`orca-c --initial-size {{columns}}x{{rows}}`

- 启动ORCA并设置最大撤销步骤数（默认为100）：

`orca-c --undo-limit {{limit}}`

- 在ORCA中显示主菜单：

`F1`

- 在ORCA中显示所有快捷键：

`?`

- 在ORCA中显示所有ORCA操作符：

`<Ctrl> + g`