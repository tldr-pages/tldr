# popd

> 从目录栈中移除通过 pushd shell 内置命令放置的目录。
> 另请参见 `pushd` 以将目录放入栈中，以及 `dirs` 以显示目录栈的内容。
> 更多信息：<https://www.gnu.org/software/bash/manual/html_node/Directory-Stack-Builtins.html>。

- 从栈中移除顶部目录并切换到该目录：

`popd`

- 移除第 N 个目录（从零开始，向左查看 `dirs` 打印的列表）：

`popd +N`

- 移除第 N 个目录（从零开始，向右查看 `dirs` 打印的列表）：

`popd -N`

- 移除第 1 个目录（从零开始，向左查看 `dirs` 打印的列表）：

`popd -n`