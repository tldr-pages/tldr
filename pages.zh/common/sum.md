# sum

> 计算文件的校验和及块数。
> 更现代的 `cksum` 的前身。
> 更多信息：<https://www.gnu.org/software/coreutils/manual/html_node/sum-invocation.html>。

- 使用 BSD 兼容算法和 1024 字节块计算校验和：

`sum {{路径/到/文件}}`

- 使用 System V 兼容算法和 512 字节块计算校验和：

`sum {{[-s|--sysv]}} {{路径/到/文件}}`
