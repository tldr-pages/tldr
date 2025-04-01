# type

> 显示 shell 将要执行的命令类型。
> 注意：所有示例均不符合 POSIX 标准。
> 更多信息：<https://www.gnu.org/software/bash/manual/bash.html#index-type>。

- 显示命令的类型：

`type {{command}}`

- 显示指定可执行文件的所有位置（仅在 Bash/fish/Zsh shell 中有效）：

`type -a {{command}}`

- 显示将要执行的磁盘文件的名称（仅在 Bash/fish/Zsh shell 中有效）：

`type -p {{command}}`

- 显示特定命令的类型，可以是别名/关键字/函数/内建命令/文件（仅在 Bash/fish shell 中有效）：

`type -t {{command}}`