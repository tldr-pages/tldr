# losetup

> Set up and control loop devices.
> More information: <https://manned.org/losetup>.

- List loop devices with detailed info:

`losetup {{[-a|--all]}}`

- Attach a file to a given loop device:

`sudo losetup {{/dev/loop}} /{{path/to/file}}`

- Attach a file to a new free loop device and scan the device for partitions:

`sudo losetup --show {{[-P|--partscan]}} {{[-f|--find]}} /{{path/to/file}}`

- Attach a file to a read-only loop device:

`sudo losetup {{[-r|--read-only]}} {{/dev/loop}} /{{path/to/file}}`

- Detach all loop devices:

`sudo losetup {{[-D|--detach-all]}}`

- Detach a given loop device:

`sudo losetup {{[-d|--detach]}} {{/dev/loop}}`
