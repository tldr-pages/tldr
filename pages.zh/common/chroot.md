# chroot

> 在特殊根目录下运行命令或交互式 shell。
> 更多信息：<https://www.gnu.org/software/coreutils/manual/html_node/chroot-invocation.html>。

- 作为新的根目录运行命令：

`chroot {{path/to/new/root}} {{command}}`

- 使用特定用户和组：

`chroot --userspec={{username_or_id:group_name_or_id}}`