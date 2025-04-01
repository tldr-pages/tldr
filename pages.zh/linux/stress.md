# stress

> 对 Linux 系统的 CPU、内存和 IO 进行压力测试。
> 更多信息：<https://manned.org/stress>.

- 启动 4 个进程以对 CPU 进行压力测试：

`stress -c {{4}}`

- 启动 2 个进程以对 IO 进行压力测试，并在 5 秒后超时：

`stress -i {{2}} -t {{5}}`

- 启动 2 个进程以对内存进行压力测试（每个进程分配 256M 字节）：

`stress -m {{2}} --vm-bytes {{256M}}`

- 启动 2 个进程进行 write()/unlink() 循环操作（每个进程写入 1G 字节）：

`stress -d {{2}} --hdd-bytes {{1GB}}`
