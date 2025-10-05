# semanage interface

> Manage SELinux network interface type definitions.
> See also: `semanage`, `semanage-port`.
> More information: <https://manned.org/semanage-interface>.

- List all interface type definitions:

`sudo semanage interface {{[-l|--list]}}`

- Add a network interface type definition:

`sudo semanage interface {{[-a|--add]}} {{[-t|--type]}} {{netif_t}} {{eth0}}`

- Delete a network interface type definition:

`sudo semanage interface {{[-d|--delete]}} {{eth0}}`

- Modify a network interface type definition:

`sudo semanage interface {{[-m|--modify]}} {{[-t|--type]}} {{ipsec_spd_t}} {{eth1}}`

- List interface type definitions in a customized format:

`sudo semanage interface -l -C`
