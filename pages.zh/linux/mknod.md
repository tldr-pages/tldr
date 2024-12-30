# mknod

> 创建块设备或字符设备特殊文件。
> 更多信息: <https://www.gnu.org/software/coreutils/mknod>。

- 创建一个块设备：

`sudo mknod {{path/to/device_file}} b {{major_device_number}} {{minor_device_number}}`

- 创建一个字符设备：

`sudo mknod {{path/to/device_file}} c {{major_device_number}} {{minor_device_number}}`

- 创建一个FIFO（队列）设备：

`sudo mknod {{path/to/device_file}} p`

- 创建一个具有默认SELinux安全上下文的设备文件：

`sudo mknod -Z {{path/to/device_file}} {{type}} {{major_device_number}} {{minor_device_number}}`