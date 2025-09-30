# udevadm

> Linux `udev` management tool.
> More information: <https://www.freedesktop.org/software/systemd/man/udevadm.html>.

- Monitor all device events:

`sudo udevadm monitor`

- Print `uevents` sent out by the kernel:

`sudo udevadm monitor {{[-k|--kernel]}}`

- Print device events after being processed by `udev`:

`sudo udevadm monitor {{[-u|--udev]}}`

- List attributes of device `/dev/sda`:

`sudo udevadm info {{[-a|--attribute-walk]}} {{/dev/sda}}`

- Reload all `udev` rules:

`sudo udevadm control {{[-R|--reload]}}`

- Trigger all `udev` rules to run:

`sudo udevadm trigger`

- Test an event run by simulating loading of `/dev/sda`:

`sudo udevadm test {{/dev/sda}}`
