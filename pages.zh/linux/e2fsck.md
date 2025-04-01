# e2fsck

> 检查 Linux ext2/ext3/ext4 文件系统。分区应已卸载。
> 更多信息：<https://manned.org/e2fsck>.

- 检查文件系统，并报告任何损坏的块：

`sudo e2fsck {{/dev/sdXN}}`

- 检查文件系统并自动修复任何损坏的块：

`sudo e2fsck -p {{/dev/sdXN}}`

- 以只读模式检查文件系统：

`sudo e2fsck -c {{/dev/sdXN}}`

- 执行详尽的、非破坏性的读写测试，检测坏块并将其列入黑名单：

`sudo e2fsck -fccky {{/dev/sdXN}}`