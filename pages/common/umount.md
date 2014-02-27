# umount

> Revokes access to an entire filesystem mounted to a directory.
> A filesystem cannot be unmounted when it is busy.

- Unmount a filesystem

`umount path_to_device_file`

- OR

`umount path_to_mounted_directory`

- Unmount all filesystems described in /etc/mtab (dangerous!)

`umount -a`
