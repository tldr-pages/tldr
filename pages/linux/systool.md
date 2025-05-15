# systool

> View system device information by bus, and classes.
> This command is part of the `sysfs` package.
> More information: <https://manned.org/systool>.

- List all attributes of devices of a bus (eg. `pci`, `usb`). View all buses using `ls /sys/bus`:

`systool -b {{bus}} -v`

- List all attributes of a class of devices (eg. `drm`, `block`). View all classes using `ls /sys/class`:

`systool -c {{class}} -v`

- Show only device drivers of a bus (eg. `pci`, `usb`):

`systool -b {{bus}} -D`
