# switch_root

> 将不同的文件系统用作挂载树的根。
> 注意：如果新根不是挂载点的根，则 `switch_root` 将无法正常工作。可以使用绑定挂载作为解决方法。
> 相关命令：`chroot`, `mount`。
> 更多信息：<https://manned.org/switch_root.8>。

- 将 `/proc`、`/dev`、`/sys` 和 `/run` 移动到指定的文件系统，将该文件系统作为新的根，并启动指定的 init 进程：

`switch_root {{new_root}} {{/sbin/init}}`

- 显示帮助：

`switch_root {{[-h|--help]}}`