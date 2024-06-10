# dd

> Convert and copy a file.
> More information: <https://manned.org/man/dd.1p>.

- Make a bootable USB drive from an isohybrid file (such as `archlinux-xxx.iso`):

`dd if={{path/to/file.iso}} of={{/dev/usb_drive}}`

- Clone a drive to another drive with 4 MiB block size and flush writes before the command terminates:

`dd bs=4194304 conv=fsync if={{/dev/source_drive}} of={{/dev/dest_drive}}`

- Generate a file with a specific number of random bytes by using kernel random driver:

`dd bs={{100}} count={{1}} if=/dev/urandom of={{path/to/random_file}}`

- Benchmark the sequential write performance of a disk:

`dd bs={{1024}} count={{1000000}} if=/dev/zero of={{path/to/file_1GB}}`

- Create a system backup, save it into an IMG file (can be restored later by swapping `if` and `of`), and show the progress:

`dd if={{/dev/drive_device}} of={{path/to/file.img}} status=progress`
