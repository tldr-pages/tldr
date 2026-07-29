# stdbuf

> 修改命令的 C 标准流（stdin、stdout、stderr）的缓冲操作。
> 更多信息：<https://www.gnu.org/software/coreutils/manual/html_node/stdbuf-invocation.html>。

- 将 stdout 的缓冲区大小更改为 1 个字节（无缓冲）：

`stdbuf -o1 {{命令}}`

- 将 stdout 的缓冲区大小更改为 1 MiB：

`stdbuf -o1M {{命令}}`

- 将 stdout 的缓冲模式更改为行缓冲：

`stdbuf -oL {{命令}}`

- 将 stderr 的缓冲区大小更改为 1 MiB：

`stdbuf -e1M {{命令}}`

- 将 stdin 的缓冲区大小更改为 512 KiB：

`stdbuf -i512K {{命令}}`
