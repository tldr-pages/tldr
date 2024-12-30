# fallocate

> 为文件保留或释放磁盘空间。
> 该工具在分配空间时不会清零。
> 更多信息：<https://manned.org/fallocate>。

- 保留一个占用 700 MiB 磁盘空间的文件：

`fallocate --length {{700M}} {{path/to/file}}`

- 将已分配的文件缩小 200 MiB：

`fallocate --collapse-range --length {{200M}} {{path/to/file}}`

- 在文件中从 100 MiB 开始缩小 20 MB 的空间：

`fallocate --collapse-range --offset {{100M}} --length {{20M}} {{path/to/file}}`