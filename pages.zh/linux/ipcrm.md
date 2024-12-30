# ipcrm

> 删除IPC（进程间通信）资源。
> 更多信息：<https://manned.org/ipcrm>。

- 通过ID删除共享内存段：

`ipcrm --shmem-id {{shmem_id}}`

- 通过键删除共享内存段：

`ipcrm --shmem-key {{shmem_key}}`

- 通过ID删除IPC队列：

`ipcrm --queue-id {{ipc_queue_id}}`

- 通过键删除IPC队列：

`ipcrm --queue-key {{ipc_queue_key}}`

- 通过ID删除信号量：

`ipcrm --semaphore-id {{semaphore_id}}`

- 通过键删除信号量：

`ipcrm --semaphore-key {{semaphore_key}}`

- 删除所有IPC资源：

`ipcrm --all`