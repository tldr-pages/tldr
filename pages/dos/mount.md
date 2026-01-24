# MOUNT

> Mount host folders/drives/images as virtual DOS drives.
> More information: <https://www.dosbox.com/wiki/MOUNT>.

- Mount current directory as C:

`MOUNT C .`

- Mount specific directory as C:

`MOUNT C {{C:\DOSGAMES}}`

- Mount with free space limit (KB):

`MOUNT C {{C:\DOSGAMES}} -freesize {{1024}}`

- Mount floppy drive:

`MOUNT A {{A:\}} -t floppy`

- Mount CD-ROM drive:

`MOUNT D {{D:\}} -t cdrom`

- Mount CD with extra options:

`MOUNT D {{D:\}} -t cdrom -usecd {{0}} -ioctl`

- Unmount drive:

`MOUNT -u {{C}}`
