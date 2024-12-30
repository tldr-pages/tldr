# duperemove

> 查找重复的文件系统范围，并可选择将其安排进行去重。
> 范围是文件系统中一个文件的小部分。
> 在某些文件系统中，当文件内容的某些部分相同时，一个范围可以被多次引用。
> 更多信息：<https://markfasheh.github.io/duperemove/>.

- 在目录中搜索重复的范围并显示它们：

`duperemove -r {{path/to/directory}}`

- 在 Btrfs 或 XFS（实验性）文件系统上去重重复的范围：

`duperemove -r -d {{path/to/directory}}`

- 使用哈希文件存储范围哈希（减少内存使用，并且可以在后续运行中重用）：

`duperemove -r -d --hashfile={{path/to/hashfile}} {{path/to/directory}}`

- 限制 I/O 线程（用于哈希和去重阶段）和 CPU 线程（用于查找重复范围阶段）：

`duperemove -r -d --hashfile={{path/to/hashfile}} --io-threads={{N}} --cpu-threads={{N}} {{path/to/directory}}`