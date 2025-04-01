# ipcmk

> 创建 IPC（进程间通信）资源。
> 更多信息：<https://manned.org/ipcmk>.

- 创建共享内存段：

`ipcmk --shmem {{segment_size_in_bytes}}`

- 创建信号量：

`ipcmk --semaphore {{element_size}}`

- 创建消息队列：

`ipcmk --queue`

- 创建具有特定权限的共享内存段（默认权限为 0644）：

`ipcmk --shmem {{segment_size_in_bytes}} {{octal_permissions}}`
