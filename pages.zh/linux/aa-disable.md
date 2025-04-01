# aa-disable

> 禁用 AppArmor 安全策略。
> 参见：`aa-complain`，`aa-enforce`，`aa-status`。
> 更多信息：<https://gitlab.com/apparmor/apparmor/-/wikis/manpage_aa-disable.8>。

- 禁用配置文件：

`sudo aa-disable {{path/to/profile1 path/to/profile2 ...}}`

- 禁用目录中的配置文件（默认为 `/etc/apparmor.d`）：

`sudo aa-disable --dir {{path/to/profiles}}`