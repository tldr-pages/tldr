# ipcrm

> حذف منابع IPC (ارتباط بین‌فرایندی).
> اطلاعات بیشتر: <https://manned.org/ipcrm>.

- حذف بخش حافظهٔ اشتراکی با شناسه:

`ipcrm {{[-m|--shmem-id]}} {{shmem_id}}`

- حذف بخش حافظهٔ اشتراکی با کلید:

`ipcrm {{[-M|--shmem-key]}} {{shmem_key}}`

- حذف صف IPC با شناسه:

`ipcrm {{[-q|--queue-id]}} {{ipc_queue_id}}`

- حذف صف IPC با کلید:

`ipcrm {{[-Q|--queue-key]}} {{ipc_queue_key}}`

- حذف سمافور با شناسه:

`ipcrm {{[-s|--semaphore-id]}} {{semaphore_id}}`

- حذف سمافور با کلید:

`ipcrm {{[-S|--semaphore-key]}} {{semaphore_key}}`

- حذف همهٔ منابع IPC:

`ipcrm {{[-a|--all]}}`
