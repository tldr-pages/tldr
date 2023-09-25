# bcachefs

> Manage bcachefs filesystems/devices.
> More information: <https://bcachefs.org/bcachefs-principles-of-operation.pdf>.

- Format a partition with bcachefs:

`sudo bcachefs format {{path/to/partition}}`

- Mount a bcachefs filesystem:

`sudo bcachefs mount {{path/to/device}} {{path/to/mountpoint}}`

- Create a RAID 0 filesystem where an SSD acts as a cache and an HDD acts as long term storage.

`sudo bcachefs format --label=ssd.ssd1 {{path/to/ssd/partition}} --label=hdd.hdd1 {{path/to/hdd/partition}} --replicas=1 --foreground_target=ssd --promote_target=ssd --background_target=hdd`
