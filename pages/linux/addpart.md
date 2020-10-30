# addpart

> Tells the Linux kernel about the existence of the specified partition.
> The command is a simple wrapper around the `add partition` ioctl.
> More information: <https://linux.die.net/man/8/addpart>.

- Tell the kernel about the existence of the specified partition:

`addpart {{device}} {{partition}} {{start}} {{length}}`
