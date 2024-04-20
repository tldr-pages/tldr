# dd

> Convert and copy a file.
> More information: <https://www.gnu.org/software/coreutils/dd>.

- Make a bootable USB drive from an isohybrid file (such as `archlinux-xxx.iso`) and show the progress:

`dd status=progress if={{path/to/file.iso}} of={{/dev/usb_drive}}`

- Clone a drive to another drive with 4 MiB block size and flush writes before the command terminates:

`dd bs={{4M}} conv={{fsync}} if={{/dev/source_drive}} of={{/dev/dest_drive}}`

- Generate a file with a specific number of random bytes by using kernel random driver:

`dd bs={{100}} count={{1}} if=/dev/urandom of={{path/to/random_file}}`

- Benchmark the write performance of a disk:

`dd bs={{1M}} count={{1000000}} if=/dev/zero of={{path/to/file_1GB}}`

- Create a system backup and save it into an IMG file (can be restored later by swapping `if` and `of`):

`dd if={{/dev/drive_device}} of={{path/to/file.img}}`

- Check the progress of an ongoing dd operation (run this command from another shell):

`kill -USR1 $(pgrep -x dd)`
