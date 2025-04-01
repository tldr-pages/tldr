# sysbench

> 基准测试系统的 CPU、IO 和内存。
> 更多信息：<https://github.com/akopytov/sysbench/>.

- 使用 1 个线程运行 10 秒的 CPU 基准测试：

`sysbench cpu run`

- 使用多个线程运行指定时间的 CPU 基准测试：

`sysbench --threads={{number_of_threads}} --time={{seconds}}`

- 使用 1 个线程运行 10 秒的内存基准测试：

`sysbench memory run`

- 准备文件系统级别的读取基准测试：

`sysbench fileio prepare`

- 运行文件系统级别的基准测试：

`sysbench --file-test-mode={{rndrd|rndrw|rndwr|seqrd|seqrewr|seqwr}} fileio run`
