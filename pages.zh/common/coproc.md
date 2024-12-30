# coproc

> Bash 内置命令，用于创建交互式异步子外壳。
> 更多信息：<https://www.gnu.org/software/bash/manual/bash.html#Coprocesses>。

- 异步运行一个子外壳：

`coproc { {{command1; command2; ...}}; }`

- 创建一个具有特定名称的协程：

`coproc {{name}} { {{command1; command2; ...}}; }`

- 向特定协程的 `stdin` 写入：

`echo "{{input}}" >&"${{{name}}[1]}"`

- 从特定协程的 `stdout` 读取：

`read {{variable}} <&"${{{name}}[0]}"`

- 创建一个协程，该协程重复读取 `stdin` 并对输入运行一些命令：

`coproc {{name}} { while read line; do {{command1; command2; ...}}; done }`

- 创建并使用一个运行 `bc` 的协程：

`coproc BC { bc --mathlib; }; echo "1/3" >&"${BC[1]}"; read output <&"${BC[0]}"; echo "$output"`