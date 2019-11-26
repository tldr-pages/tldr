# ddrescue

> GNU ddrescue is a data recovery tool. It copies data from one file or block device (hard disc, cdrom, etc) to another, trying to rescue the good parts first in case of read errors.  https://www.gnu.org/software/ddrescue/.

- Take an image of a device, creating a log file:

`sudo ddrescue {{/dev/sdb}} {{path/to/image.dd}} {{path/to/ddrescue.log}}`

- Clone Disk A to Disk B, creating a log file:

`sudo ddrescue --force --no-scrape {{/dev/sda}} {{/dev/sdb}} {{path/to/ddrescue.log}}`
