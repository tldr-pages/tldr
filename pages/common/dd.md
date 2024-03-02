# dd

> Convert and copy a file.
> More information: <https://www.gnu.org/software/coreutils/dd>.

- Make a bootable USB drive from an isohybrid file (such like `archlinux-xxx.iso`) and show progress:

`dd status=progress if={{path/to/file.iso}} of=/dev/{{usb_drive}}`

- Clone a drive to another drive with 4 MiB block and ignore error:

`dd if=/dev/{{source_drive}} of=/dev/{{dest_drive}} bs={{4194304}} conv={{noerror}}`

- Generate a file of 100 random bytes by using kernel random driver:

`dd if=/dev/urandom of={{path/to/random_file}} bs={{100}} count={{1}}`

- Benchmark the sequential write performance of a disk:

`dd if=/dev/zero of={{path/to/file_1GB}} bs={{1024}} count={{1000000}}`

- Generate a system backup into an IMG file (can be restored later by swapping `if` with `of`):

`dd if={{/dev/drive_device}} of={{path/to/file.img}}`
