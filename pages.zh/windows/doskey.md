# doskey

> 管理宏、窗口命令和命令行。
> 更多信息：<https://learn.microsoft.com/windows-server/administration/windows-commands/doskey>。

- 列出可用的宏：

`doskey /macros`

- 创建一个新的宏：

`doskey {{name}} = "{{command}}"`

- 为特定可执行文件创建一个新的宏：

`doskey /exename={{executable}} {{name}} = "{{command}}"`

- 删除一个宏：

`doskey {{name}} =`

- 显示存储在内存中的所有命令：

`doskey /history`

- 将宏保存到文件以便于移植：

`doskey /macros > {{path\to\macinit_file}}`

- 从文件加载宏：

`doskey /macrofile = {{path\to\macinit_file}}`