# udevadm

> Linux `udev` management tool.
> More information: <https://linux.die.net/man/8/udevadm>.

- Monitor device events:

`sudo udevadm monitor [--kernel] [--udev]`

- List attributes of a device:

`sudo udevadm info --attribute-walk --path {{/dev/sda1}}`

- Reload all `udev` rules:

`sudo udevadm control --reload-rules`

- Trigger all `udev` rules to run:

`sudo udevadm trigger`
