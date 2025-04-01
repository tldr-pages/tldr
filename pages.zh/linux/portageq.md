# portageq

> 查询与 Gentoo Linux 软件包管理器 Portage 相关的信息。
> 可查询的 Portage 特定环境变量列于 `/var/db/repos/gentoo/profiles/info_vars`。
> 更多信息：<https://wiki.gentoo.org/wiki/Portageq>。

- 显示 Portage 特定环境变量的值：

`portageq envvar {{variable}}`

- 显示配置了 Portage 的存储库的详细列表：

`portageq repos_config /`

- 按优先级（最高优先级在前）显示存储库列表：

`portageq get_repos /`

- 显示关于原子（即包括版本的软件包名称）的特定元数据：

`portageq metadata / {{ebuild|porttree|binary|...}} {{category}}/{{package}} {{BDEPEND|DEFINED_PHASES|DEPEND|...}}`
