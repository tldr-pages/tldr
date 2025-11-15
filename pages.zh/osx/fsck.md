# fsck

> 检查或修复文件系统的完整性，运行命令时应卸载文件系统。
> 它是一个包装器，包含 `fsck_hfs`, `fsck_apfs`, `fsck_msdos`, `fsck_exfat`, `fsck_udf` 作为可选。
> 更多信息：<https://keith.github.io/xcode-man-pages/fsck.8.html>.

- 检查文件系统 /dev/sda，报告损坏的块：

`fsck {{/dev/sda}}`

- 仅当文件系统 /dev/sda 是干净的时才检查它，报告任何损坏的块并以交互方式让用户选择修复每个块：

`fsck -f {{/dev/sda}}`

- 仅当文件系统 /dev/sda 干净时才检查它，报告任何损坏的块并自动修复它们：

`fsck -fy {{/dev/sda}}`

- 检查文件系统 /dev/sda, 报告是否已完全卸载：

`fsck -q {{/dev/sda}}`
