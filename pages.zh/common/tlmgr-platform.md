# tlmgr 平台

> 管理 TeX Live 平台。
> 更多信息：<https://www.tug.org/texlive/tlmgr.html>。

- 列出软件包库中所有可用的平台：

`tlmgr platform list`

- 为特定平台添加可执行文件：

`sudo tlmgr platform add {{platform}}`

- 移除特定平台的可执行文件：

`sudo tlmgr platform remove {{platform}}`

- 自动检测并切换到当前平台：

`sudo tlmgr platform set auto`

- 切换到特定平台：

`sudo tlmgr platform set {{platform}}`