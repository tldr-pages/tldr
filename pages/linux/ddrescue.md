# ddrescue

> Data recovery tool that reads data from damaged block devices.
> More information: <https://www.gnu.org/software/ddrescue/>.

- Take an image of a device, creating a log file:

`sudo ddrescue {{/dev/sdb}} {{path/to/image.dd}} {{path/to/log.txt}}`

- Clone Disk A to Disk B, creating a log file:

`sudo ddrescue --force --no-scrape {{/dev/sda}} {{/dev/sdb}} {{path/to/log.txt}}`
