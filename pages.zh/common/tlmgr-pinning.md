# tlmgr pinning

> pinning 动作管理固定文件。
> 更多信息：<https://www.tug.org/texlive/doc/tlmgr.html#pinning>.

- 显示当前的固定数据：

`tlmgr pinning show`

- 将匹配的软件包固定到指定的仓库：

`tlmgr pinning add {{repository}} {{package1 package2 ...}}`

- 移除指定仓库中记录的与给定软件包匹配的固定数据：

`tlmgr pinning remove {{repository}} {{package1 package2 ...}}`

- 移除指定仓库的所有固定数据：

`tlmgr pinning remove {{repository}} --all`
