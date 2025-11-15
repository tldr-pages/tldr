# cmd

> Windows 命令解释器。
> 更多信息：<https://learn.microsoft.com/windows-server/administration/windows-commands/cmd>.

- 开启一个新的命令行实例：

`cmd`

- 运行指定的命令然后退出：

`cmd /c {{echo 命令}}`

- 执行一个指定的命令，之后进入一个交互式 shell：

`cmd /k {{echo 命令}}`

- 不显示命令的输出结果：

`cmd /q`

- 启用或禁用环境变量扩展：

`cmd /v:{{on|off}}`

- 启用或禁用命令扩展：

`cmd /e:{{on|off}}`

- 强制输出内容使用 Unicode 编码：

`cmd /u`
