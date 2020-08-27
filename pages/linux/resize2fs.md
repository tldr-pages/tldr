# resize2fs

> Resize an ext2, ext3 or ext4 file system.
> Does not resize the underlying partition.
> File system must be unmounted.

- Automatically resize file system:

`resize2fs {{/dev/sda1}}`

- Resize the file system to 40G with a percentage completion bar:

`resize2fs -p {{/dev/sda1}} 40G`

- Shrink the file system to its minimum possible size:

`resize2fs -M {{/dev/sda1}}`
