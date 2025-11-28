# nvme

> NVMe storage user space utility.
> More information: <https://github.com/linux-nvme/nvme-cli>.

- List all nvme devices:

`sudo nvme list`

- Show device information:

`sudo nvme smart-log {{device}}`

- Secure erase user data on nvme device:

`sudo nvme format {{[-s|--ses]}} 1 {{[-n|--namespace]}} {{[-r|--reset]}} {{device}}`
