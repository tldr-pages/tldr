# exec

> 执行命令而不创建子进程。
> 更多信息：<https://www.gnu.org/software/bash/manual/bash.html#index-exec>。

- 执行特定命令：

`exec {{command -with -flags}}`

- 在几乎空的环境中执行命令：

`exec -c {{command -with -flags}}`

- 作为登录 shell 执行命令：

`exec -l {{command -with -flags}}`

- 使用不同的名称执行命令：

`exec -a {{name}} {{command -with -flags}}`