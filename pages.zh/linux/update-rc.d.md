# update-rc.d

> 安装和删除 System-V 风格的 init 脚本链接服务。
> init 脚本位于 `/etc/init.d/`。
> 更多信息：<https://manned.org/update-rc.d>.

- 安装一个服务：

`update-rc.d {{mysql}} defaults`

- 启用一个服务：

`update-rc.d {{mysql}} enable`

- 禁用一个服务：

`update-rc.d {{mysql}} disable`

- 强制删除一个服务：

`update-rc.d -f {{mysql}} remove`
