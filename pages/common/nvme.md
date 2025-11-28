# nvme

> NVMe storage user space utility.
> More information: <https://github.com/linux-nvme/nvme-cli>.

- List all nvme devices:

`sudo nvme list`

- Show device information:

`sudo nvme smart-log {{device}}`

- Secure erase user data on nvme device:

`sudo nvme format -s1 {{-n|--namespace}} {{-r|--reset}} {{device}}`   

- Refresh devices after erase to check if successful 

`sudo partprobe`
