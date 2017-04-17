# dd

> dd is a utility that allows copying many different forms of
> data from one location or disk to another location or disk, block by block

- Copy a bootable ISO to a USB Stick or SDCard

`dd if={{img_file}} of={{disk_device_location}} bs=4m count=1`

- Securely wipe the contents of a file or disk by overwriting it with zeros

`dd if=/dev/zero of={{file_or_disk}} bs=4m`
