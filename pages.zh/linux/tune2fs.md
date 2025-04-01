# tune2fs

> 调整 ext2、ext3 或 ext4 文件系统的参数。
> 可用于已挂载的文件系统。
> 更多信息：<https://manned.org/tune2fs>。

- 设置文件系统在检查前的最大计数为 2：

`tune2fs -c {{2}} {{/dev/sdXN}}`

- 将文件系统的标签设置为 MY_LABEL：

`tune2fs -L {{'MY_LABEL'}} {{/dev/sdXN}}`

- 为文件系统启用 discard 和用户指定的扩展属性：

`tune2fs -o {{discard,user_xattr}} {{/dev/sdXN}}`

- 为文件系统启用日志记录：

`tune2fs -o^{{nobarrier}} {{/dev/sdXN}}`