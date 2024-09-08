# dd

> Convert and copy a file.
> More information: <https://keith.github.io/xcode-man-pages/dd.1.html>.

- Make a bootable USB drive from an isohybrid file (such like `archlinux-xxx.iso`) and show the progress:

`dd if={{path/to/file.iso}} of={{/dev/usb_drive}} status=progress`

- Clone a drive to another drive with 4 MB block, ignore error and show the progress:

`dd bs=4m conv=noerror if={{/dev/source_drive}} of={{/dev/dest_drive}} status=progress`

- Generate a file with a specific number of random bytes by using kernel random driver:

`dd bs={{100}} count={{1}} if=/dev/urandom of={{path/to/random_file}}`

- Benchmark the write performance of a disk:

`dd bs={{1024}} count={{1000000}} if=/dev/zero of={{path/to/1GB_file}}`

- Create a system backup, save it into an IMG file (can be restored later by swapping `if` and `of`), and show the progress:

`dd if={{/dev/drive_device}} of={{path/to/file.img}} status=progress`

- Check the progress of an ongoing `dd` operation (run this command from another shell):

`kill -USR1 $(pgrep ^dd)`
