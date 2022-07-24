# fstab

> /etc/fstab automatically mounts partitions with different options.
> It is not a command, but a text file you edit with an editor of choice.
> More information: <https://manned.org/fstab>.

- The file is seperated into different sections for each partition you want to auto-mount:

`UUID/Label | Directory to mount to | Type of the partition | Options for mounting | Dump | Order in which partitions are read by 'fsck'`

- Here you put the "UUID" of the partition you wish to auto-mount. You can get the UUID by running: `sudo blkid`. You can also define this with Partition Labels, if you have that:

`UUID/Label`

- Tell fstab where to mount your partition to, for example: `/media/Harddrive`. Be aware that the directory needs to exist before you can mount to it. Create the directory you want with 'mkdir':

`Directory`

- Put the type of your partition here. To figure out what partition type your partition is, run: `sudo blkid`:

`Type of the partition`

- Here you can tell fstab what additional settings you want to mount your partition with. Seperate each option with , (without spaces inbetween):

`Options for mounting`

- These Options aren't as important, you can just set them both to 0. Pass: Tell fstab which partitions to check first on boot (with fsck):

`Dump/Pass`
