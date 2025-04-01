# dnf config-manager

> 管理基于 Fedora 系统的 DNF 配置选项和仓库。
> 更多信息：<https://manned.org/dnf-config-manager>。

- 从 URL 添加（并启用）一个仓库：

`dnf config-manager --add-repo={{repository_url}}`

- 打印当前配置值：

`dnf config-manager --dump`

- 启用特定的仓库：

`dnf config-manager --set-enabled {{repository_id}}`

- 禁用指定的仓库：

`dnf config-manager --set-disabled {{repository_id1 repository_id2 ...}}`

- 为仓库设置配置选项：

`dnf config-manager --setopt={{option}}={{value}}`

- 显示帮助：

`dnf config-manager --help-cmd`