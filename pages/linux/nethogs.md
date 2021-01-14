# nethogs

> Monitor bandwidth usage per process.
> More information: <https://github.com/raboof/nethogs>.

- Start nethogs as root (default device is eth0):

`sudo nethogs`

- Monitor bandwidth on specific device:

`sudo nethogs {{device}}`

- Monitor bandwidth on multiple devices:

`sudo nethogs {{device1}} {{device2}}`

- Specify refresh rate:

`sudo nethogs -t {{seconds}}`
