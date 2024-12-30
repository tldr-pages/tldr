# fsck

> 检查文件系统的完整性或修复它。在运行该命令时，文件系统应处于未挂载状态。
> 它是一个包装器，根据需要调用 `fsck_hfs`、`fsck_apfs`、`fsck_msdos`、`fsck_exfat` 和 `fsck_udf`。
> 更多信息：<https://keith.github.io/xcode-man-pages/fsck.8.html>。

- 检查文件系统 `/dev/sdX`，报告任何损坏的块：

`fsck {{/dev/sdX}}`

- 仅在文件系统干净时检查 `/dev/sdX`，报告任何损坏的块并让用户互动选择修复每一个：

`fsck -f {{/dev/sdX}}`

- 仅在文件系统干净时检查 `/dev/sdX`，报告任何损坏的块并自动修复它们：

`fsck -fy {{/dev/sdX}}`

- 检查文件系统 `/dev/sdX`，报告它是否已被干净地卸载：

`fsck -q {{/dev/sdX}}`