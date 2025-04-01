# chroot

> 以特殊根目录运行命令或交互式 shell。
> 更多信息：<https://www.gnu.org/software/coreutils/manual/html_node/chroot-invocation.html>.

- 以新的根目录运行命令：

`sudo chroot {{path/to/new/root}} {{command}}`

- 使用特定的用户和组：

`sudo chroot --userspec {{username_or_id:group_name_or_id}}`
