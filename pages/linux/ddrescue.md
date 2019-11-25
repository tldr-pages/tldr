# ddrescue

> GNU ddrescue is a data recovery tool.
> It copies data from one file or block device (hard disc, cdrom, etc)
> to another, trying to rescue the good parts first in case of read errors.
> https://www.gnu.org/software/ddrescue/

- Make an image (image.dd) of /dev/sdb in the current directory, and make a log:
`sudo ddrescue {{/dev/sdb}} {{image.dd}} {{ddrescue.log}}`

- Clone Disk A to Disk B and make a log:
`sudo ddrescue -f -n {{/dev/sda}} {{/dev/sdb}} {{/home/$USER/ddrescue.log}}'
