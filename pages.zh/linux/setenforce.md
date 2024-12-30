# setenforce

> 切换 SELinux 处于强制和宽容模式。
> 要启用或禁用 SELinux，请改为编辑 `/etc/selinux/config`。
> 另请参见：`getenforce`，`semanage-permissive`。
> 更多信息：<https://manned.org/setenforce>。

- 将 SELinux 设置为强制模式：

`setenforce {{1|强制}}`

- 将 SELinux 设置为宽容模式：

`setenforce {{0|宽容}}`