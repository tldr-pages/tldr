# tlmgr 仓库

> 管理 TeX Live 安装的仓库。
> 更多信息：<https://www.tug.org/texlive/tlmgr.html>。

- 列出所有配置的仓库及其标签（如果设置）：

`tlmgr repository list`

- 列出特定仓库中所有可用的包：

`tlmgr repository list {{路径|网址|标签}}`

- 添加一个带有特定标签的新仓库（标签不是必需的）：

`sudo tlmgr repository add {{路径|网址}} {{标签}}`

- 移除一个特定的仓库：

`sudo tlmgr repository remove {{路径|网址|标签}}`

- 设置一个新的仓库列表，覆盖之前的列表：

`sudo tlmgr repository set {{路径|网址|标签}}#{{标签}} {{路径|网址|标签}}#{{标签}} {{...}}`

- 显示所有配置的仓库的验证状态：

`tlmgr repository status`