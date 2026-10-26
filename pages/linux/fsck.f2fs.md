# fsck.f2fs

> Check an F2FS filesystem and optionally repair it. The filesystem should be unmounted.
> More information: <https://manned.org/fsck.f2fs>.

- Check a filesystem:

`sudo fsck.f2fs {{/dev/sdXY}}`

- [a]utomatically fix a filesystem when the kernel has reported a bug:

`sudo fsck.f2fs -a {{/dev/sdXY}}`

- [f]orce repair of every inconsistency:

`sudo fsck.f2fs -f {{/dev/sdXY}}`

- Check a filesystem and answer [N]o to every question:

`sudo fsck.f2fs -N {{/dev/sdXY}}`

- Show the stored directory [t]ree:

`sudo fsck.f2fs -t {{/dev/sdXY}}`

- Show every filename and inode number stored in the image:

`sudo fsck.f2fs -M {{/dev/sdXY}}`
