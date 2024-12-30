# eselect 仓库

> 一个用于配置 Portage 的 ebuild 仓库的 `eselect` 模块。
> 启用仓库后，您需要运行 `emerge --sync repo_name` 来下载 ebuild。
> 更多信息请访问：<https://wiki.gentoo.org/wiki/Eselect/Repository>。

- 列出所有注册在 <https://repos.gentoo.org> 上的 ebuild 仓库：

`eselect repository list`

- 列出已启用的仓库：

`eselect repository list -i`

- 通过名称或 `list` 命令中的索引启用列表中的仓库：

`eselect repository enable {{name|index}}`

- 启用一个未注册的仓库：

`eselect repository add {{name}} {{rsync|git|mercurial|svn|...}} {{sync_uri}}`

- 禁用仓库而不删除其内容：

`eselect repository disable {{repo1 repo2 ...}}`

- 禁用仓库并删除其内容：

`eselect repository remove {{repo1 repo2 ...}}`

- 创建一个本地仓库并启用它：

`eselect repository create {{name}} {{path/to/repo}}`