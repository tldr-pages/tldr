# ifne

> 根据 `stdin` 的是否为空来运行命令。
> 更多信息：<https://joeyh.name/code/moreutils/>.

- 仅当 `stdin` 不为空时运行指定的命令：

`ifne {{command options ...}}`

- 仅当 `stdin` 为空时运行指定的命令，否则将 `stdin` 传递给 `stdout`：

`ifne -n {{command options ...}}`