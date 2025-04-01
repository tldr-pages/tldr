# systemd-sysext

> 激活或停用系统扩展镜像。
> 更多信息：<https://www.freedesktop.org/software/systemd/man/systemd-sysext.html>.

- 列出已安装的扩展镜像：

`systemd-sysext list`

- 将系统扩展镜像合并到 `/usr/` 和 `/opt/`：

`systemd-sysext merge`

- 检查当前的合并状态：

`systemd-sysext status`

- 从 `/usr/` 和 `/opt/` 卸载所有当前已安装的系统扩展镜像：

`systemd-sysext unmerge`

- 刷新系统扩展镜像（先卸载再合并）：

`systemd-sysext refresh`
