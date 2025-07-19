# btrfs device

> Manage devices in a btrfs filesystem.
> More information: <https://btrfs.readthedocs.io/en/latest/btrfs-device.html>.

- Add one or more devices to a btrfs filesystem:

`sudo btrfs {{[d|device]}} {{[a|add]}} {{path/to/block_device1 path/to/block_device2 ...}} {{path/to/btrfs_filesystem}}`

- Remove a device from a btrfs filesystem:

`sudo btrfs {{[d|device]}} {{[rem|remove]}} {{path/to/device1|device_id1 path/to/device2|device_id2 ...}}`

- Display error statistics:

`sudo btrfs {{[d|device]}} {{[st|stats]}} {{path/to/btrfs_filesystem}}`

- Scan all disks and inform the kernel of all detected btrfs filesystems:

`sudo btrfs {{[d|device]}} {{[sc|scan]}} {{[-d|--all-devices]}}`

- Display detailed per-disk allocation statistics:

`sudo btrfs {{[d|device]}} {{[u|usage]}} {{path/to/btrfs_filesystem}}`
