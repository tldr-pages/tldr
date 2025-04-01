# dirs

> 显示或操纵目录栈。
> 目录栈是一个最近访问过的目录列表，可以使用 `pushd` 和 `popd` 命令进行操作。
> 更多信息：<https://www.gnu.org/software/bash/manual/bash.html#Directory-Stack-Builtins>.

- 显示目录栈，每条目之间用空格分隔：

`dirs`

- 显示目录栈，每条目占一行：

`dirs -p`

- 显示目录栈中的第 `n` 个条目，从 0 开始计数：

`dirs +{{n}}`

- 清空目录栈：

`dirs -c`