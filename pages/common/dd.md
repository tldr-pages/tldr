# dd

> Copy and convert a file.  Useful for working with disk images and whole storage devices.

- Make a disk image of the entire filesystem of device /dev/sda and save it as the file disk1.img in your home folder:

`dd if=/dev/sda of=~/disk1.img`

- Take the filesystem in disk1.img and write it to /dev/sda, overwriting any old filesystem:

`dd if=~/disk1.img of=/dev/sda`

- Same as above but specifying a block size of 2048 during copying (smaller block size means longer transfer time but less chance of filesystem corruption):

`dd if=~/disk1.img of=/dev/sda bs=2048`
