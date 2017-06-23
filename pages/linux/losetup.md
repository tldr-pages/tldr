# losetup

> Set up and control loop devices.

- List loop devices with detailed info:

`losetup -a`

- Associate / Attach a device or file to a {{loop}} device:

`sudo losetup /dev/{{loop}} /{{path/to/<file>}}`

- Detach All {{loop}} devices:

`sudo losetup -D`

- Detach a specific {{loop}} device:

`sudo losetup -d /dev/{{loop}}`
