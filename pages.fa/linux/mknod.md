# mknod

> ایجاد فایل‌های ویژهٔ دستگاه بلوکی یا نویسه‌ای.
> اطلاعات بیشتر: <https://www.gnu.org/software/coreutils/manual/html_node/mknod-invocation.html>.

- ایجاد دستگاه بلوکی:

`sudo mknod {{path/to/device_file}} b {{major_device_number}} {{minor_device_number}}`

- ایجاد دستگاه نویسه‌ای:

`sudo mknod {{path/to/device_file}} c {{major_device_number}} {{minor_device_number}}`

- ایجاد دستگاه FIFO (صف):

`sudo mknod {{path/to/device_file}} p`

- ایجاد فایل دستگاه با زمینهٔ امنیتی پیش‌فرض SELinux:

`sudo mknod {{[-Z|--context]}} {{path/to/device_file}} {{type}} {{major_device_number}} {{minor_device_number}}`
