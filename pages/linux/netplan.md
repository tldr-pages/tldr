# netplan

> Network configuration utility using YAML.
> More information: <https://netplan.readthedocs.io/en/stable/cli/>.

- Apply a network configuration and make it persistent:

`sudo netplan apply`

- Generate backend configuration files:

`sudo netplan generate`

- Configure a network interface to use DHCP:

`sudo netplan set ethernets.{{interface_name}}.dhcp4=true`

- Try configuration changes without applying them permanently:

`sudo netplan try --timeout {{seconds}}`

- Return to previous working configuration after failed apply:

`sudo netplan --debug apply`

- Display the current netplan configuration status:

`netplan status`
