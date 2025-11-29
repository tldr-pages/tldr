# nvme

> NVMe storage user space utility.
> More information: <https://manned.org/nvme>.

- List all NVMe devices:

`sudo nvme list`

- Show device information:

`sudo nvme smart-log {{device}}`

- Secure erase user data on NVMe device:

`sudo nvme format {{[-s|--ses]}} 1 {{[-r|--reset]}} {{device}}`
