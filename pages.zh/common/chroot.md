# chroot

> 使用指定的根目录运行命令或交互式 shell。
> 更多信息：<https://www.gnu.org/software/coreutils/manual/html_node/chroot-invocation.html>.

- 以新的根目录，运行命令：

`sudo chroot {{路径/到/新/根目录}} {{命令}}`

- 使用指定的用户和组：

`sudo chroot --userspec {{用户名或用户id:组名或组id}}`
