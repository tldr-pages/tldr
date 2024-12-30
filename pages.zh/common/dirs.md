# dirs

> 显示或操作目录栈。
> 目录栈是一个最近访问过的目录列表，可以使用 `pushd` 和 `popd` 命令进行操作。
> 更多信息：<https://www.gnu.org/software/bash/manual/bash.html#Directory-Stack-Builtins>。

- 以空格分隔显示目录栈：

`dirs`

- 逐行显示目录栈，每行一个条目：

`dirs -p`

- 仅显示目录栈中的第 n 个条目，从 0 开始：

`dirs +{{N}}`

- 清空目录栈：

`dirs -c`