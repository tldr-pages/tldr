# lsipc

> نمایش اطلاعات امکانات IPC از نوع System V که اکنون در سیستم استفاده می‌شوند.
> همچنین ببینید: `ipcs`.
> اطلاعات بیشتر: <https://manned.org/lsipc>.

- نمایش اطلاعات همهٔ امکانات IPC فعال:

`lsipc`

- نمایش اطلاعات بخش‌های حافظهٔ اشتراکی، صف‌های پیام یا مجموعه‌های سمافور فعال:

`lsipc {{--shmems|--queues|--semaphores}}`

- نمایش جزئیات کامل منبع با شناسهٔ مشخص:

`lsipc {{--shmems|--queues|--semaphores}} {{[-i|--id]}} {{resource_id}}`

- چاپ ستون‌های خروجی مشخص (همهٔ ستون‌های پشتیبانی‌شده را با `--help` ببینید):

`lsipc {{[-o|--output]}} {{KEY,ID,PERMS,SEND,STATUS,NSEMS,RESOURCE,...}}`

- استفاده از قالب خام، JSON، فهرست یا صادرات (key="value"):

`lsipc {{--raw|--json|--list|--export}}`

- کوتاه نکردن خروجی:

`lsipc --notruncate`
