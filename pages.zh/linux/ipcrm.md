# ipcrm

> 删除 IPC（进程间通信）资源。
> 更多信息：<https://manned.org/ipcrm>.

- 通过 ID 删除共享内存段：

`ipcrm {{[-m|--shmem-id]}} {{shmem_id}}`

- 通过键删除共享内存段：

`ipcrm {{[-M|--shmem-key]}} {{shmem_key}}`

- 通过 ID 删除 IPC 队列：

`ipcrm {{[-q|--queue-id]}} {{ipc_queue_id}}`

- 通过键删除 IPC 队列：

`ipcrm {{[-Q|--queue-key]}} {{ipc_queue_key}}`

- 通过 ID 删除信号量：

`ipcrm {{[-s|--semaphore-id]}} {{semaphore_id}}`

- 通过键删除信号量：

`ipcrm {{[-S|--semaphore-key]}} {{semaphore_key}}`

- 删除所有 IPC 资源：

`ipcrm {{[-a|--all]}}`