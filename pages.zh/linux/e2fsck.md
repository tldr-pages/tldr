# e2fsck

> 检查 Linux ext2/ext3/ext4 文件系统。分区应该被卸载。
> 更多信息：<https://manned.org/e2fsck>。

- 检查文件系统，报告任何损坏的块：

`sudo e2fsck {{/dev/sdXN}}`

- 检查文件系统并自动修复任何损坏的块：

`sudo e2fsck -p {{/dev/sdXN}}`

- 以只读模式检查文件系统：

`sudo e2fsck -c {{/dev/sdXN}}`

- 执行全面的非破坏性读写测试以查找坏块并将其列入黑名单：

`sudo e2fsck -fccky {{/dev/sdXN}}`