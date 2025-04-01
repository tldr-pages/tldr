# sum

> 计算文件的校验和和块数。
> 是较现代的 `cksum` 命令的前身。
> 更多信息：<https://www.gnu.org/software/coreutils/manual/html_node/sum-invocation.html>.

- 使用与 BSD 兼容的算法和 1024 字节块计算校验和：

`sum {{path/to/file}}`

- 使用与 System V 兼容的算法和 512 字节块计算校验和：

`sum {{[-s|--sysv]}} {{path/to/file}}`