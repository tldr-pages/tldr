# doskey

> 管理宏，Windows 命令和命令行。
> 更多信息：<https://learn.microsoft.com/windows-server/administration/windows-commands/doskey>.

- 列出可用的宏：

`doskey /macros`

- 创建一个新的宏：

`doskey {{宏的名称}} = "{{命令}}"`

- 为指定可执行文件创建新的宏：

`doskey /exename={{可执行文件名}} {{宏的名称}} = "{{命令}}"`

- 删除一个宏：

`doskey {{宏的名称}} =`

- 列出所有储存在内存中的命令：

`doskey /history`

- 将宏保存到文件以便于移植：

`doskey /macros > {{保存宏的文件名}}`

- 从文件中加载宏：

`doskey /macrofile = {{保存宏的文件名}}`
