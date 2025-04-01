# bgpgrep

> 过滤并打印 MRT 转储文件中的 BGP 数据。
> 可以读取使用 `gzip`、`bzip2` 和 `xz` 压缩的文件。
> 更多信息：<https://codeberg.org/1414codeforge/ubgpsuite>。

- 列出所有路由：

`bgpgrep {{master6.mrt}}`

- 列出从特定对等方接收的路由，通过对等方的 AS 号确定：

`bgpgrep {{master4.mrt}} -peer {{64498}}`

- 列出从特定对等方接收的路由，通过对等方的 IP 地址确定：

`bgpgrep {{master4.mrt.bz2}} -peer {{2001:db8:dead:cafe:acd::19e}}`

- 列出 AS 路径中包含特定 AS 编号的路由：

`bgpgrep {{master6.mrt.bz2}} -aspath '{{64498 64510}}'`

- 列出通往特定地址的路由：

`bgpgrep {{master6.mrt.bz2}} -supernet '{{2001:db8:dead:cafe:aef::5}}'`

- 列出具有来自特定 AS 的共同体的路由：

`bgpgrep {{master4.mrt}} -communities \( '{{64497}}:*' \)`
