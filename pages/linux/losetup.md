# losetup

> Set up and control loop devices.

- List loop devices with detailed info:

`losetup -a`

- Attach a file to a given loop device:

`sudo losetup /dev/{{loop}} /{{path/to/file}}`

- Detach all loop devices:

`sudo losetup -D`

- Detach a given loop device:

`sudo losetup -d /dev/{{loop}}`

- Attach a file to a new free loop device and scan the device for partitions:

`sudo losetup --show --partscan -f /{{path/to/file}}`

- Attach a file to a read-only loop device:

`sudo losetup --read-only /dev/{{loop}} /{{path/to/file}}`
