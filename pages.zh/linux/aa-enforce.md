# aa-enforce

> 将 AppArmor 配置文件设置为强制模式。
> 参见：`aa-complain`, `aa-disable`, `aa-status`。
> 更多信息：<https://gitlab.com/apparmor/apparmor/-/wikis/manpage_aa-enforce.8>。

- 启用配置文件：

`sudo aa-enforce --dir {{path/to/profile}}`

- 启用多个配置文件：

`sudo aa-enforce {{path/to/profile1 path/to/profile2 ...}}`
