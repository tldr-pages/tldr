# pfetch

> 显示系统信息。
> 更多信息：<https://github.com/dylanaraps/pfetch>.

- 显示 ASCII 艺术和默认字段：

`pfetch`

- 仅显示 ASCII 艺术和颜色调色板字段：

`PF_INFO="{{ascii palette}}" pfetch`

- 显示所有可能的字段：

`PF_INFO="{{ascii title os host kernel uptime pkgs memory shell editor wm de palette}}" pfetch`

- 显示不同的用户名和主机名：

`USER="{{user}}" HOSTNAME="{{hostname}}" pfetch`

- 不使用颜色显示：

`PF_COLOR={{0}} pfetch`
