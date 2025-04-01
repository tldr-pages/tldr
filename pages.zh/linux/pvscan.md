# pvscan

> 列出所有物理卷并管理其在线状态。
> 更多信息：<https://manned.org/pvscan>.

- 列出所有物理卷：

`pvscan`

- 显示使用特定物理卷的卷组：

`pvscan --cache --listvg {{/dev/sdX}}`

- 显示使用特定物理卷的逻辑卷：

`pvscan --cache --listlvs {{/dev/sdX}}`

- 以 JSON 格式显示详细信息：

`pvscan --reportformat json`