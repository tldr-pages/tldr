# dd

> Convert and copy a file or image.

- Clone a hard disk to another disk:

`dd if=/dev/sda of=/dev/sdb`

- Backi up a partition to a file:

`dd if=/dev/sda2 of=~/sdadisk.img`

- Crate a USB flash installation media:

`dd bs=4M if=/path/to/my_awesome_linux.iso of=/dev/sdx status=progress oflag=sync`

- Wipe content of a disk:

`dd if=/dev/zero of=/dev/sdb`

- Create ISO files from a CD-ROM or DVD-ROM or USB flash drives:

`dd if=/dev/dvd of=/opt/my_awesome_linux.iso`
