# dd

> Convert and copy a file.

- Make a bootable usb drive from an isohybrid file (such like archlinux-xxx.iso):

`dd if={{file.iso}} of=/dev/{{usb_drive}}`

- Clone a drive to another drive with 4MB block and ignore error:

`dd if=/dev/{{source_drive}} of=/dev/{{dest_drive}} bs=4m conv=noerror`

- Generate a file of 100 random bytes by using kernel random driver:

`dd if=/dev/urandom of={{random_file}} bs=100 count=1`

- Benchmark the write performance of a disk:

`dd if=/dev/zero of={{file_1GB}} bs=1024 count=1000000`
