# fsck.btrfs

> Exit successfully without checking a filesystem. Btrfs does not need a traditional filesystem check before mount.
> To check or repair a filesystem, use `btrfs check`. Set the `fs_passno` field in `/etc/fstab` to 0.
> More information: <https://btrfs.readthedocs.io/en/latest/fsck.btrfs.html>.

- Print a message that points to `btrfs check`:

`sudo fsck.btrfs {{/dev/sdXY}}`

- Exit successfully without printing that message, as boot-time checks do with `-a`, `-A`, `-p`, or `-y`:

`sudo fsck.btrfs -a {{/dev/sdXY}}`

- View documentation for checking or repairing a btrfs filesystem:

`tldr btrfs check`
