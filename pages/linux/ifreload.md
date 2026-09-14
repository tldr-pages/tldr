# ifreload

> Reload network interface configuration.
> More information: <https://manned.org/ifreload>.

- Reload all network interface configurations:

`sudo ifreload -a`

- Reload a specific network interface:

`sudo ifreload {{interface}}`

- Reload interfaces and print detailed output:

`sudo ifreload -v`

- Check the configuration without applying changes:

`sudo ifreload -c`
