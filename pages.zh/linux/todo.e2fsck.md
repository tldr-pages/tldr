# e2fsck

> Check a Linux ext2/ext3/ext4 filesystem. The filesystem should be unmounted at the time the command is run.

- Check filesystem, reporting any damaged blocks:

`e2fsck {{/dev/sdXN}}`

- Check filesystem and automatically repair any damaged blocks:

`e2fsck -p {{/dev/sdXN}}`

- Check filesystem in read only mode:

`e2fsck -c {{/dev/sdXN}}`
