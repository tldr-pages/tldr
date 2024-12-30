# bmaptool

> 智能创建或复制块映射（旨在比 `cp` 或 `dd` 更快）。
> 更多信息：<https://source.tizen.org/documentation/reference/bmaptool>。

- 从映像文件输出块映射文件：

`bmaptool create -o {{blockmap.bmap}} {{source.img}}`

- 将映像文件复制到 sdb：

`bmaptool copy --bmap {{blockmap.bmap}} {{source.img}} {{/dev/sdb}}`

- 将压缩的映像文件复制到 sdb：

`bmaptool copy --bmap {{blockmap.bmap}} {{source.img.gz}} {{/dev/sdb}}`

- 不使用块映射将映像文件复制到 sdb：

`bmaptool copy --nobmap {{source.img}} {{/dev/sdb}}`