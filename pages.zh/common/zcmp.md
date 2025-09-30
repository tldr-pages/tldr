# zcmp

> 比较压缩文件。
> 更多信息：<https://manned.org/zcmp>.

- 对两个通过 `gzip` 压缩的文件运行 `cmp` 命令：

`zcmp {{路径/到/文件1.gz}} {{路径/到/文件2.gz}}`

- 将一个文件与其 gzipped 版本进行比较（假设 `.gz` 已存在）：

`zcmp {{路径/到/文件}}`
