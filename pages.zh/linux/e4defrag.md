# e4defrag

> 对 ext4 文件系统进行碎片整理。
> 更多信息：<https://manned.org/e4defrag>。

- 碎片整理文件系统：

`e4defrag {{/dev/sdXN}}`

- 查看文件系统的碎片情况：

`e4defrag -c {{/dev/sdXN}}`

- 在每个文件之前和之后打印错误和碎片计数：

`e4defrag -v {{/dev/sdXN}}`