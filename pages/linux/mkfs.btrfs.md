# mkfs.btrfs

> Create a btrfs filesystem.
> Defaults to `raid1`, which specifies 2 copies of a given data block spread across 2 different devices.
> More information: <https://btrfs.wiki.kernel.org/index.php/Manpage/mkfs.btrfs>.

- Create a btrfs filesystem on a single device:

`sudo mkfs.btrfs --metadata single --data single {{/dev/sda}}`

- Create a btrfs filesystem on multiple devices with raid1:

`sudo mkfs.btrfs --metadata raid1 --data raid1 {{/dev/sda}} {{/dev/sdb}} {{/dev/sdN}}`

- Set a label for the filesystem:

`sudo mkfs.btrfs --label "{{label}}" {{/dev/sda}} [{{/dev/sdN}}]`
