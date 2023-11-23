# systemd-machine-id-setup

> Initialize the machine ID stored in `/etc/machine-id` at install time with a provisioned or randomly generated ID.
> Note: Always use `sudo` to execute these commands as they require elevated privileges.
> More information: <https://www.freedesktop.org/software/systemd/man/systemd-machine-id-setup.html>.

- Print the generated or committed machine ID:

`systemd-machine-id-setup --print`

- Specify an image policy:

`systemd-machine-id-setup --image-policy={{your_policy}}`

- Display the output as JSON:

`sudo systemd-machine-id-setup --json=pretty`

- Operate on a disk image instead of a directory tree:

`systemd-machine-id-setup --image={{/path/to/image}}`
