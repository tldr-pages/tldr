# nethogs

> Monitor bandwidth usage per process.
> More information: <https://manned.org/nethogs>.

- Start NetHogs as root (default device is `eth0`):

`sudo nethogs`

- Monitor bandwidth on specific device:

`sudo nethogs {{device}}`

- Monitor bandwidth on multiple devices:

`sudo nethogs {{device1 device2 ...}}`

- Specify refresh interval in seconds:

`sudo nethogs -d {{seconds}}`

- Change the traffic display unit (default: 0, 0 = kB/s, 1 = total kB, 2 = total bytes, 3 = total MB, 4 = MB/s, 5 = GB/s):

`sudo nethogs -v {{0|1|2|3|4|5}}`
