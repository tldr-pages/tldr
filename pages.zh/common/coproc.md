# coproc

> Bash 内置命令，用于创建交互式异步子壳层。
> 更多信息：<https://www.gnu.org/software/bash/manual/bash.html#Coprocesses>.

- 异步运行子壳层：

`coproc { {{command1; command2; ...}}; }`

- 创建具有特定名称的协程：

`coproc {{name}} { {{command1; command2; ...}}; }`

- 向特定协程的 `stdin` 写入：

`echo "{{input}}" >&"${{{name}}[1]}"`

- 从特定协程的 `stdout` 读取：

`read {{variable}} <&"${{{name}}[0]}"`

- 创建一个持续读取 `stdin` 并在输入上运行某些命令的协程：

`coproc {{name}} { while read line; do {{command1; command2; ...}}; done }`

- 创建一个持续读取 `stdin`，在输入上运行管道命令，并将输出写入 `stdout` 的协程：

`coproc {{name}} { while read line; do echo "$line" | {{command1 | command2 | ...}} | cat /dev/fd/0; done }`

- 创建并使用运行 `bc` 的协程：

`coproc BC { bc --mathlib; }; echo "1/3" >&"${BC[1]}"; read output <&"${BC[0]}"; echo "$output"`