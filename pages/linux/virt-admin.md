# virt-admin

> `virt-admin` program is the main administration interface for modifying the libvirt daemon configuration at runtime, changing daemon behaviour as well as for monitoring and managing all clients connected to the daemon.
> Some subcommands for the interacting with the `daemon`, `server`, and `client` have their own usage documentation.
> More information: <https://manned.org/virt-admin.1>.

- See help information:

`virt-admin --help`

- Print the libvirt library virt-admin is coming from, `long` will give more details with a link to the libvirt website:

`virt-admin --version=[short|long]`

- Avoid extra informational messages when entering `virt-admin`:

`virt-admin --quiet`

- Enable debug messages at the integer _LEVEL_ and above, levels range 1-4 with 4 being the default:

`virt-admin --debug [ 1 | 2 | 3 | 4(default) ]`

- Connect to the specified _URI_:

`virt-admin --connect virtqemud:///system`
