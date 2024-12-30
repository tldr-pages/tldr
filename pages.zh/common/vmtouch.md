# vmtouch

> 管理文件系统缓存。
> 更多信息：<https://manned.org/vmtouch>。

- 打印文件的缓存状态：

`vmtouch {{path/to/file}}`

- 将文件加载到缓存中：

`vmtouch -t {{path/to/file}}`

- 从缓存中驱逐文件：

`vmtouch -e {{path/to/file}}`

- 锁定文件在缓存中，以防止从内存中驱逐：

`vmtouch -l {{path/to/file}}`

- 锁定文件并将程序作为守护进程运行：

`vmtouch -ld {{path/to/file}}`