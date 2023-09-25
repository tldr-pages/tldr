# bcachefs

> Manage bcachefs filesystems/devices.
> More information: <https://bcachefs.org/bcachefs-principles-of-operation.pdf>.

- Format a partition with bcachefs:

`sudo bcachefs format {{path/to/partition}}`

- Mount a bcachefs filesystem:

`sudo bcachefs mount {{path/to/device}} {{path/to/mountpoint}}`
