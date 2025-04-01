# rankmirrors

> 根据连接和打开速度对 Pacman 镜像列表进行排序。
> 将新的镜像列表写入 `stdout`。
> 更多信息：<https://manned.org/rankmirrors>。

- 对镜像列表进行排序：

`rankmirrors {{/etc/pacman.d/mirrorlist}}`

- 仅输出排序最高的指定数量的服务器：

`rankmirrors -n {{number}} {{/etc/pacman.d/mirrorlist}}`

- 在生成镜像列表时显示详细信息：

`rankmirrors -v {{/etc/pacman.d/mirrorlist}}`

- 仅测试特定的 URL：

`rankmirrors --url {{url}}`

- 仅输出响应时间而不是完整的镜像列表：

`rankmirrors --times {{/etc/pacman.d/mirrorlist}}`
