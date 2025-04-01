# duperemove

> 查找文件系统中重复的数据块，并可选择安排这些数据块进行去重。
> 数据块是文件系统内部文件的一个小部分。
> 在某些文件系统中，当文件内容的部分相同，一个数据块可以被多次引用。
> 更多信息：<https://markfasheh.github.io/duperemove/>.

- 在目录中查找重复的数据块并显示它们：

`duperemove -r {{path/to/directory}}`

- 对 Btrfs 或 XFS（实验性）文件系统中的重复数据块进行去重：

`duperemove -r -d {{path/to/directory}}`

- 使用哈希文件存储数据块哈希值（减少内存使用并在后续运行中重用）：

`duperemove -r -d --hashfile={{path/to/hashfile}} {{path/to/directory}}`

- 限制 I/O 线程（用于哈希和去重阶段）和 CPU 线程（用于查找重复数据块阶段）：

`duperemove -r -d --hashfile={{path/to/hashfile}} --io-threads={{n}} --cpu-threads={{n}} {{path/to/directory}}`
