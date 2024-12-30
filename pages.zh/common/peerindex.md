# peerindex

> 检查 MRT TABLE_DUMPV2 对等索引表。
> 可以读取使用 `gzip`、`bzip2` 和 `xz` 压缩的文件。
> 更多信息：<https://codeberg.org/1414codeforge/ubgpsuite>。

- 列出所有对等体：

`peerindex {{master6.mrt}}`

- 显示所有提供路由信息的对等体：

`peerindex -r {{master6.mrt}}`