# dnf group

> 管理基于 Fedora 的系统上的虚拟软件包集合。
> 更多信息：<https://manned.org/dnf-group>.

- 列出 DNF 组，以表格形式显示已安装和未安装的状态：

`dnf group list`

- 显示 DNF 组信息，包括仓库和可选软件包：

`dnf group info {{group_name}}`

- 安装 DNF 组：

`dnf group install {{group_name}}`

- 删除 DNF 组：

`dnf group remove {{group_name}}`

- 升级 DNF 组：

`dnf group upgrade {{group_name}}`
