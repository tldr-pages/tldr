# e4defrag

> 对 ext4 文件系统进行碎片整理。
> 更多信息：<https://manned.org/e4defrag>.

- 对文件系统进行碎片整理：

`e4defrag {{/dev/sdXN}}`

- 查看文件系统的碎片程度：

`e4defrag -c {{/dev/sdXN}}`

- 打印每个文件整理前后的错误和碎片数量：

`e4defrag -v {{/dev/sdXN}}`