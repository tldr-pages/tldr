# makensis

> 跨平台 NSIS 安装程序编译器。
> 它将 NSIS 脚本编译成 Windows 安装程序可执行文件。
> 更多信息：<https://nsis.sourceforge.io/Docs/Chapter3.html>。

- 编译 NSIS 脚本：

`makensis {{path/to/file.nsi}}`

- 严格模式编译 NSIS 脚本（将警告视为错误）：

`makensis -WX {{path/to/file.nsi}}`

- 显示特定命令的帮助：

`makensis -CMDHELP {{command}}`
