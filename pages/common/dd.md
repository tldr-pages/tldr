# dd

> Convert and copy a file.
> More information: <https://www.gnu.org/software/coreutils/dd>.

- Make a bootable usb drive from an isohybrid file (such like `archlinux-xxx.iso`) and show the progress:

`dd if={{file.iso}} of=/dev/{{usb_drive}} status=progress`

- Clone a drive to another drive with 4MB block, ignore error and show progress:

`dd if=/dev/{{source_drive}} of=/dev/{{dest_drive}} bs=4M conv=noerror status=progress`

- Generate a file of 100 random bytes by using kernel random driver:

`dd if=/dev/urandom of={{random_file}} bs=100 count=1`

- Benchmark the write performance of a disk:

`dd if=/dev/zero of={{file_1GB}} bs=1024 count=1000000`

- Check progress of an ongoing dd operation (Run this command from another shell):

`kill -USR1 $(pgrep ^dd)`
