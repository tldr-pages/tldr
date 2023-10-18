# dd

> Convert and copy a file.
> More information: <https://keith.github.io/xcode-man-pages/dd.1.html>.

- Make a bootable USB drive from an isohybrid file (such like `archlinux-xxx.iso`) and show the progress:

`dd if={{path/to/file.iso}} of={{/dev/usb_device}} status=progress`

- Clone a drive to another drive with 4 MB block, ignore error and show the progress:

`dd if={{/dev/source_device}} of={{/dev/dest_device}} bs={{4m}} conv={{noerror}} status=progress`

- Generate a file of 100 random bytes by using kernel random driver:

`dd if=/dev/urandom of={{path/to/random_file}} bs={{100}} count={{1}}`

- Benchmark the write performance of a disk:

`dd if=/dev/zero of={{path/to/1GB_file}} bs={{1024}} count={{1000000}}`

- Generate a system backup into an IMG file and show the progress:

`dd if=/dev/{{drive_device}} of={{path/to/file.img}} status=progress`

- Restore a drive from an IMG file and show the progress:

`dd if={{path/to/file.img}} of={{/dev/drive_device}} status=progress`

- Check the progress of an ongoing dd operation (run this command from another shell):

`kill -USR1 $(pgrep ^dd)`
