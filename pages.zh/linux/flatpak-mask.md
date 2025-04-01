# flatpak mask

> 阻止更新和自动安装。
> 更多信息：<https://docs.flatpak.org/en/latest/flatpak-command-reference.html#flatpak-mask>.

- 忽略特定 flatpak 的更新：

`flatpak mask {{com.example.app}}`

- 撤销忽略更新：

`flatpak mask --remove {{com.example.app}}`

- 列出所有当前被屏蔽的模式：

`flatpak mask {{--system|--user}}`
