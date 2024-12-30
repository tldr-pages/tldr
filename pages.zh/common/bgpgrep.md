# bgpgrep

> 过滤并打印MRT转储中的BGP数据。
> 可以读取使用 `gzip`、`bzip2` 和 `xz` 压缩的文件。
> 更多信息：<https://codeberg.org/1414codeforge/ubgpsuite>。

- 列出所有路由：

`bgpgrep {{master6.mrt}}`

- 列出从特定对等体接收到的路由，通过对等体的AS号确定：

`bgpgrep {{master4.mrt}} -peer {{64498}}`

- 列出从特定对等体接收到的路由，通过对等体的IP地址确定：

`bgpgrep {{master4.mrt.bz2}} -peer {{2001:db8:dead:cafe:acd::19e}}`

- 列出在其AS路径中具有特定ASN的路由：

`bgpgrep {{master6.mrt.bz2}} -aspath '{{64498 64510}}'`

- 列出指向特定地址的路由：

`bgpgrep {{master6.mrt.bz2}} -supernet '{{2001:db8:dead:cafe:aef::5}}'`

- 列出具有来自特定AS的社区的路由：

`bgpgrep {{master4.mrt}} -communities \( '{{64497}}:*' \)`