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

- Change the traffic display unit (e.g. 3 for total MB, 4 for MB/s):

`sudo nethogs -v {{view_mode}}`
