# tune2fs

> Adjust parameters of an ext2, ext3 or ext4 filesystem.
> May be used on mounted filesystems.
> More information: <https://manned.org/tune2fs>.

- Set the max number of counts before a filesystem is checked to 2:

`sudo tune2fs -c 2 {{/dev/sdXN}}`

- Set the filesystem label to MY_LABEL:

`sudo tune2fs -L 'MY_LABEL' {{/dev/sdXN}}`

- Enable discard and user-specified extended attributes for a filesystem:

`sudo tune2fs -o discard,user_xattr {{/dev/sdXN}}`

- Enable journaling for a filesystem:

`sudo tune2fs -o has_journal {{/dev/sdXN}}`

- Assign a new randomly-generated UUID to a filesystem:

`sudo tune2fs -U random {{/dev/sdXN}}`
