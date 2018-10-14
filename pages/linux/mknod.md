# mknod

> Create block or character device special files.

- Create block device:

`sudo mknod {{/path/to/device_file}} b {{major_device_number}} {{minor_device_number}}`

- Create character device:

`sudo mknod {{/path/to/device_file}} c {{major_device_number}} {{minor_device_number}}`

- Create FIFO (queue) device:

`sudo mknod {{/path/to/device_file}} p`

- Create device file with default SELinux security context:

`sudo mknod -Z {{/path/to/device_file}} {{type}} [{{major_device_number}} {{minor_device_number}}]`

