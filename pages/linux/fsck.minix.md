# fsck.minix

> Check the consistency of a Minix filesystem. The filesystem should be unmounted.
> More information: <https://manned.org/fsck.minix>.

- Check a filesystem:

`sudo fsck.minix {{/dev/sdXY}}`

- [l]ist every filename:

`sudo fsck.minix {{[-l|--list]}} {{/dev/sdXY}}`

- Perform interactive [r]epairs:

`sudo fsck.minix {{[-r|--repair]}} {{/dev/sdXY}}`

- Perform [a]utomatic repairs (this can destroy a badly damaged filesystem):

`sudo fsck.minix {{[-a|--auto]}} {{/dev/sdXY}}`

- [f]orce a check even when the filesystem is marked valid:

`sudo fsck.minix {{[-f|--force]}} {{/dev/sdXY}}`

- Output [s]uper-block information:

`sudo fsck.minix {{[-s|--super]}} {{/dev/sdXY}}`

- Display help:

`sudo fsck.minix {{[-h|--help]}}`

- Display version:

`sudo fsck.minix {{[-V|--version]}}`
