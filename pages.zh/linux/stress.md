# 压力测试

> 在Linux系统上对CPU、内存和IO进行压力测试。
> 更多信息：<https://manned.org/stress>。

- 启动4个工作进程进行CPU压力测试：

`stress -c {{4}}`

- 启动2个工作进程进行IO压力测试，5秒后超时：

`stress -i {{2}} -t {{5}}`

- 启动2个工作进程进行内存压力测试（每个工作进程分配256M字节）：

`stress -m {{2}} --vm-bytes {{256M}}`

- 启动2个工作进程进行写入()/unlink()压力测试（每个工作进程写入1G字节）：

`stress -d {{2}} --hdd-bytes {{1GB}}`