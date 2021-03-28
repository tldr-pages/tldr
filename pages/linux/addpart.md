# addpart

> Tells the Linux kernel about the existence of the specified partition.
> The command is a simple wrapper around the `add partition` ioctl.
> More information: <https://www.man7.org/linux/man-pages/man8/addpart.8.html>.

- Tell the kernel about the existence of the specified partition:

`addpart {{device}} {{partition}} {{start}} {{length}}`
