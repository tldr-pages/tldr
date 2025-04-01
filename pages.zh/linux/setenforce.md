# setenforce

> 在强制模式和宽容模式之间切换 SELinux。
> 要启用或禁用 SELinux，请编辑 `/etc/selinux/config` 文件。
> 参见：`getenforce`，`semanage-permissive`。
> 更多信息：<https://manned.org/setenforce>。

- 将 SELinux 设置为强制模式：

`setenforce {{1|Enforcing}}`

- 将 SELinux 设置为宽容模式：

`setenforce {{0|Permissive}}`
