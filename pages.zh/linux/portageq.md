# portageq

> 查询有关Portage的信息，Portage是Gentoo Linux的包管理器。
> 可查询的Portage特定环境变量列在`/var/db/repos/gentoo/profiles/info_vars`中。
> 更多信息：<https://wiki.gentoo.org/wiki/Portageq>。

- 显示Portage特定环境变量的值：

`portageq envvar {{variable}}`

- 显示使用Portage配置的仓库的详细列表：

`portageq repos_config /`

- 按优先级（最高优先级在前）显示仓库列表：

`portageq get_repos /`

- 显示有关原子（即包括版本的包名称）的特定元数据：

`portageq metadata / {{ebuild|porttree|binary|...}} {{category}}/{{package}} {{BDEPEND|DEFINED_PHASES|DEPEND|...}}`