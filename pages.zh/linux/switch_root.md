# switch_root

> 使用不同的文件系统作为挂载树的根。
> 注意：如果新根不是一个挂载的根，switch_root 将无法正常工作。可以使用绑定挂载作为解决方法。
> 另请参见：`chroot`, `mount`。
> 更多信息：<https://manned.org/switch_root.8>。

- 将 `/proc`、`/dev`、`/sys` 和 `/run` 移动到指定文件系统，使用该文件系统作为新根，并启动指定的初始化进程：

`switch_root {{new_root}} {{/sbin/init}}`

- 显示帮助信息：

`switch_root -h`