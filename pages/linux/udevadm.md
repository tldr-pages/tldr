# udevadm

> Linux `udev` management tool.
> More information: <https://www.freedesktop.org/software/systemd/man/udevadm>.

- Monitor all device events:

`sudo udevadm monitor`

- Print `uevents` sent out by the kernel:

`sudo udevadm monitor --kernel`

- Print device events after rule processing by `udev`:

`sudo udevmadm monitor --udev`

- List attributes of a device:

`sudo udevadm info --attribute-walk --path {{/dev/sda1}}`

- Reload all `udev` rules:

`sudo udevadm control --reload-rules`

- Trigger all `udev` rules to run:

`sudo udevadm trigger`
