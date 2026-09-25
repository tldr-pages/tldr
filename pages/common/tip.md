# tip

> Connect to a remote system or serial console.
> More information: <https://manned.org/tip>.

- Connect to a remote system defined in `/etc/remote`:

`tip {{system_name}}`

- Connect at a specific baud rate:

`tip -{{115200}} {{system_name}}`

- Connect with verbose output:

`tip -v {{system_name}}`

- Connect with tilde escape sequences disabled:

`tip -n {{system_name}}`
