# dd

> Convert and copy files to disks/partitions, and vice-versa. Commonly used to burn image files to USB sticks, or create an image of a disk. Further info: https://linux.die.net/man/1/dd

> Be very careful when using this and double-check your commands! A common nickname for this command is "disk destroyer"...
- Copy/burn an image file to a disk:

`sudo dd if={{source_file}} of={{disk_name}}`

`if` is input, `of` is output. Note, the desired disk name can be found with the command `lsblk` and is in the format of `/dev/sdx`.

- Create an image of a disk:

`sudo dd if={{disk_name}} of={{image_file.iso}}`
