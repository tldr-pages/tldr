# cmd

> Windows 命令解释器。
> 更多信息：<https://learn.microsoft.com/windows-server/administration/windows-commands/cmd>。

- 启动一个交互式 shell 会话：

`cmd`

- 执行特定的 [c]ommands：

`cmd /c {{echo Hello world}}`

- 执行特定脚本：

`cmd {{path\to\script.bat}}`

- 执行特定命令后进入交互式 shell：

`cmd /k {{echo Hello world}}`

- 启动一个交互式 shell 会话，命令输出中禁用 `echo`：

`cmd /q`

- 启动一个交互式 shell 会话，启用或禁用延迟 [v]ariable 扩展：

`cmd /v:{{on|off}}`

- 启动一个交互式 shell 会话，启用或禁用命令 [e]xtensions：

`cmd /e:{{on|off}}`

- 启动一个交互式 shell 会话，使用 [u]nicode 编码：

`cmd /u`