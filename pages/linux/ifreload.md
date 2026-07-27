# ifreload

> Reload network interface configuration.
> More information: <https://manned.org/ifreload>.

- Reload all interfaces marked as "auto" in the interfaces file:

`ifreload -a`

- Reload only the interfaces that are currently up:

`ifreload -c`

- Reload all "auto" interfaces with verbose output:

`ifreload -v -a`

- Check the syntax of the interfaces file without applying any changes:

`ifreload -s`

- Reload all "auto" interfaces while excluding specific ones:

`ifreload -a -X "eth0"`
