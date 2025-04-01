# tlmgr repository

> 管理 TeX Live 安装的仓库。
> 更多信息：<https://www.tug.org/texlive/tlmgr.html>。

- 列出所有已配置的仓库及其标签（如果已设置）：

`tlmgr repository list`

- 列出特定仓库中所有可用的软件包：

`tlmgr repository list {{path|url|tag}}`

- 添加一个新的仓库并指定标签（标签不是必需的）：

`sudo tlmgr repository add {{path|url}} {{tag}}`

- 移除特定的仓库：

`sudo tlmgr repository remove {{path|url|tag}}`

- 设置新的仓库列表，覆盖之前的列表：

`sudo tlmgr repository set {{path|url|tag}}#{{tag}} {{path|url|tag}}#{{tag}} {{...}}`

- 显示所有已配置仓库的验证状态：

`tlmgr repository status`