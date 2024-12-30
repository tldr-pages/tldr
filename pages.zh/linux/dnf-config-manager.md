# dnf 配置管理器

> 管理基于 Fedora 的系统上的 DNF 配置选项和软件源。
> 更多信息：<https://manned.org/dnf-config-manager>。

- 从 URL 添加（并启用）一个软件源：

`dnf config-manager --add-repo={{repository_url}}`

- 打印当前配置值：

`dnf config-manager --dump`

- 启用特定的软件源：

`dnf config-manager --set-enabled {{repository_id}}`

- 禁用指定的软件源：

`dnf config-manager --set-disabled {{repository_id1 repository_id2 ...}}`

- 为软件源设置配置选项：

`dnf config-manager --setopt={{option}}={{value}}`

- 显示帮助：

`dnf config-manager --help-cmd`