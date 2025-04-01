# fallocate

> 预留或释放文件的磁盘空间。
> 该工具在分配空间时不会进行清零操作。
> 更多信息：<https://manned.org/fallocate>.

- 预留一个占用 700 MiB 磁盘空间的文件：

`fallocate {{[-l|--length]}} {{700M}} {{path/to/file}}`

- 将已分配的文件减小 200 MiB：

`fallocate {{[-c|--collapse-range]}} {{[-l|--length]}} {{200M}} {{path/to/file}}`

- 从文件的 100 MiB 处开始，减少 20 MiB 的空间：

`fallocate {{[-c|--collapse-range]}} {{[-o|--offset]}} {{100M}} {{[-l|--length]}} {{20M}} {{path/to/file}}`
