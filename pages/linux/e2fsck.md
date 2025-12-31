# e2fsck

> Check a Linux ext2/ext3/ext4 filesystem. The partition should be unmounted.
> More information: <https://manned.org/e2fsck>.

- Check filesystem, reporting any damaged blocks:

`sudo e2fsck {{/dev/sdXN}}`

- Check filesystem and automatically repair ([p]reen) any damaged blocks:

`sudo e2fsck -p {{/dev/sdXN}}`

- Check filesystem in read only mode:

`sudo e2fsck -c {{/dev/sdXN}}`

- [f]orce checking even if the filesystem seems clean:

`sudo e2fsck -f {{/dev/sdXN}}`

- Perform an exhaustive, non-destructive read-write test for bad blocks and blacklist them:

`sudo e2fsck -fccky {{/dev/sdXN}}`
