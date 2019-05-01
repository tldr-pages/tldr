# mknod

> Create block or character device special files.

- Create a block device:

`sudo mknod {{path/to/device_file}} b {{major_device_number}} {{minor_device_number}}`

- Create a character device:

`sudo mknod {{path/to/device_file}} c {{major_device_number}} {{minor_device_number}}`

- Create a FIFO (queue) device:

`sudo mknod {{path/to/device_file}} p`

- Create a device file with default SELinux security context:

`sudo mknod -Z {{path/to/device_file}} {{type}} {{major_device_number}} {{minor_device_number}}`
