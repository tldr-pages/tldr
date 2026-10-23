# fsck.f2fs

> Check and repair an F2FS filesystem. The filesystem should be unmounted at the time the command is run.
> More information: <https://manned.org/fsck.f2fs>.

- Check the F2FS filesystem on a device for errors:

`sudo fsck.f2fs {{/dev/sdXN}}`

- Force a check and fix all inconsistencies found in the partition:

`sudo fsck.f2fs -f {{/dev/sdXN}}`

- Run the check in [a]uto-fix mode, which only runs if a bug was reported by the F2FS kernel module:

`sudo fsck.f2fs -a {{/dev/sdXN}}`

- Check the filesystem, answering [N]o to all repair questions so nothing is modified:

`sudo fsck.f2fs -N {{/dev/sdXN}}`

- Show every directory entry stored in the partition:

`sudo fsck.f2fs -t {{/dev/sdXN}}`

- Show a file [M]ap: all filenames and inode numbers stored in the filesystem:

`sudo fsck.f2fs -M {{/dev/sdXN}}`

- Check the filesystem with a given [d]ebugging message level:

`sudo fsck.f2fs -d {{level}} {{/dev/sdXN}}`
