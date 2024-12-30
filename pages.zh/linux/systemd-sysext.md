# systemd-sysext

> 激活或停用系统扩展映像。
> 更多信息：<https://www.freedesktop.org/software/systemd/man/systemd-sysext.html>。

- 列出已安装的扩展映像：

`systemd-sysext list`

- 将系统扩展映像合并到 `/usr/` 和 `/opt/`：

`systemd-sysext merge`

- 检查当前合并状态：

`systemd-sysext status`

- 从 `/usr/` 和 `/opt/` 中取消合并所有当前安装的系统扩展映像：

`systemd-sysext unmerge`

- 刷新系统扩展映像（`unmerge` 和 `merge` 的组合）：

`systemd-sysext refresh`