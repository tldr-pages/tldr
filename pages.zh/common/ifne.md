# ifne

> 根据 `stdin` 是否为空来执行命令。
> 更多信息：<https://joeyh.name/code/moreutils/>.

- 只有当 `stdin` 不为空时，才执行指定的命令：

`ifne {{command options ...}}`

- 只有当 `stdin` 为空时，才执行指定的命令，否则将 `stdin` 传递到 `stdout`：

`ifne -n {{command options ...}}`
