# sum

> 计算文件的校验和和块数。
> 这是较现代的 `cksum` 的前身。
> 更多信息：<https://www.gnu.org/software/coreutils/sum>。

- 使用 BSD 兼容算法和 1024 字节块计算校验和：

`sum {{path/to/file}}`

- 使用 System V 兼容算法和 512 字节块计算校验和：

`sum --sysv {{path/to/file}}`