# orca-c

> ORCA live 编程环境的 C 语言版本。
> ORCA 是一种用于创建过程化序列器的编程语言。
> 更多信息：<https://github.com/hundredrabbits/Orca-c>.

- 用空白工作区启动 ORCA：

`orca-c`

- 启动 ORCA 并打开特定文件：

`orca-c {{path/to/file.orca}}`

- 启动 ORCA 并设置特定的拍速（默认为 120）：

`orca-c --bpm {{beats_per_minute}}`

- 启动 ORCA 并设置网格的大小：

`orca-c --initial-size {{columns}}x{{rows}}`

- 启动 ORCA 并设置最大的撤销步骤数（默认为 100）：

`orca-c --undo-limit {{limit}}`

- 在 ORCA 中显示主菜单：

`<F1>`

- 在 ORCA 中显示所有快捷键：

`<?>`

- 在 ORCA 中显示所有操作符：

`<Ctrl g>`