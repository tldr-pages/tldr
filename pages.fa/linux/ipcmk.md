# ipcmk

> ایجاد منابع IPC (ارتباط بین‌فرایندی).
> اطلاعات بیشتر: <https://manned.org/ipcmk>.

- ایجاد بخش حافظهٔ اشتراکی:

`ipcmk {{[-M|--shmem]}} {{segment_size_in_bytes}}`

- ایجاد سمافور:

`ipcmk {{[-S|--semaphore]}} {{element_size}}`

- ایجاد صف پیام:

`ipcmk {{[-Q|--queue]}}`

- ایجاد بخش حافظهٔ اشتراکی با مجوزهای مشخص (پیش‌فرض 0644 است):

`ipcmk {{[-M|--shmem]}} {{segment_size_in_bytes}} {{octal_permissions}}`
