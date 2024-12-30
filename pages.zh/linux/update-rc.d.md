# update-rc.d

> 安装和移除以 System-V 风格的初始化脚本链接的服务。
> 初始化脚本位于 `/etc/init.d/`。
> 更多信息：<https://manned.org/update-rc.d>。

- 安装服务：

`update-rc.d {{mysql}} defaults`

- 启用服务：

`update-rc.d {{mysql}} enable`

- 禁用服务：

`update-rc.d {{mysql}} disable`

- 强制移除服务：

`update-rc.d -f {{mysql}} remove`