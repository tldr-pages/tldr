# fsck

> 检查文件系统的完整性或修复它。在运行命令时，文件系统应该处于卸载状态。
> 更多信息：<https://manned.org/fsck>。

- 检查文件系统 `/dev/sdXN`，报告任何损坏的块：

`sudo fsck {{/dev/sdXN}}`

- 检查文件系统 `/dev/sdXN`，报告任何损坏的块，并互动地让用户选择修复每一个：

`sudo fsck -r {{/dev/sdXN}}`

- 检查文件系统 `/dev/sdXN`，报告任何损坏的块并自动修复它们：

`sudo fsck -a {{/dev/sdXN}}`