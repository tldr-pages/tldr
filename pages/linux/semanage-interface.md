# semanage interface

> Manage SELinux network interface type definitions.
> See also: `semanage`, `semanage-port`.
> More information: <https://manned.org/semanage-interface>.

- List all interface type definitions:

`sudo semanage interface {{[-l|--list]}}`

- Add a network interface type definition:

`sudo semanage interface {{[-a|--add]}} {{[-t|--type]}} {{type_name}} {{interface_name}}`

- Delete a network interface type definition:

`sudo semanage interface {{[-d|--delete]}} {{interface_name}}`

- Modify a network interface type definition:

`sudo semanage interface {{[-m|--modify]}} {{[-t|--type]}} {{type_name}} {{interface_name}}`

- List interface type definitions in a customized format:

`sudo semanage interface {{[-l|--list]}} {{[-C|--locallist]}}`
