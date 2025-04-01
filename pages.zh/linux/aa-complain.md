# aa-complain

> 将 AppArmor 策略设置为报告模式。
> 参见：`aa-disable`，`aa-enforce`，`aa-status`。
> 更多信息：<https://gitlab.com/apparmor/apparmor/-/wikis/manpage_aa-complain.8>。

- 将策略设置为报告模式：

`sudo aa-complain {{path/to/profile1 path/to/profile2 ...}}`

- 将多个策略设置为报告模式：

`sudo aa-complain --dir {{path/to/profiles}}`
