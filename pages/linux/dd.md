# dd

> Convert and copy a file.
> More information: <https://www.gnu.org/software/coreutils/dd>.

- Make a bootable USB drive from an isohybrid file (such like `archlinux-xxx.iso`) and show the progress:

`dd if={{path/to/file.iso}} of={{/dev/usb_drive}} status=progress`

- Clone a drive to another drive with 4 MiB block, ignore error and show the progress:

`dd if={{/dev/source_drive}} of={{/dev/dest_drive}} bs={{4M}} conv={{noerror}} status=progress`

- Generate a file of 100 random bytes by using kernel random driver:

`dd if=/dev/urandom of={{path/to/random_file}} bs={{100}} count={{1}}`

- Benchmark the write performance of a disk:

`dd if=/dev/zero of={{path/to/file_1GB}} bs={{1024}} count={{1000000}}`

- Generate a system backup into an IMG file and show the progress:

`dd if={{/dev/drive_device}} of={{path/to/file.img}} status=progress`

- Restore a drive from an IMG file and show the progress:

`dd if={{path/to/file.img}} of={{/dev/drive_device}} status=progress`

- Check the progress of an ongoing dd operation (run this command from another shell):

`kill -USR1 $(pgrep ^dd)`
