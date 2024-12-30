# aa-status

> 列出当前加载的 AppArmor 模块。
> 另见：`aa-complain`、`aa-disable`、`aa-enforce`。
> 更多信息：<https://gitlab.com/apparmor/apparmor/-/wikis/manpage_aa-status.8>。

- 检查状态：

`sudo aa-status`

- 显示加载的策略数量：

`sudo aa-status --profiled`

- 显示加载的强制策略数量：

`sudo aa-status --enforced`

- 显示加载的非强制策略数量：

`sudo aa-status --complaining`

- 显示加载的强制策略中会终止任务的数量：

`sudo aa-status --kill`