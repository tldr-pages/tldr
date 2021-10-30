# btrfs device

> Manage devices in a btrfs filesystem.
> More information: <https://btrfs.wiki.kernel.org/index.php/Manpage/btrfs-device>.

- Add one or more devices to a btrfs filesystem:

`sudo btrfs device add {{path/to/block_device1}} [{{path/to/block_device2}}] {{path/to/btrfs_filesystem}}`

- Remove a device from a btrfs filesystem:

`sudo btrfs device remove {{path/to/device|device_id}} [{{...}}]`

- Display error statistics:

`sudo btrfs device stats {{path/to/btrfs_filesystem}}`

- Scan all disks and inform the kernel of all detected btrfs filesystems:

`sudo btrfs device scan --all-devices`

- Display detailed per-disk allocation statistics:

`sudo btrfs device usage {{path/to/btrfs_filesystem}}`
