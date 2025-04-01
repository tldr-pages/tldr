# fsck

> 检查或修复文件系统的完整性。执行命令时文件系统应已卸载。
> 更多信息：<https://manned.org/fsck>.

- 检查文件系统 `/dev/sdXN`，报告任何损坏的块：

`sudo fsck {{/dev/sdXN}}`

- 检查文件系统 `/dev/sdXN`，报告任何损坏的块并交互式地让用户选择修复每个块：

`sudo fsck -r {{/dev/sdXN}}`

- 检查文件系统 `/dev/sdXN`，报告任何损坏的块并自动修复它们：

`sudo fsck -a {{/dev/sdXN}}`
