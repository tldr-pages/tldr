# ansible-inventory

> Display or dump an Ansible inventory.
> See also: `ansible`.
> More information: <https://www.ansible.com>.

- Display the default inventory:

`ansible-inventory --list`

- Display a custom inventory:

`ansbile-inventory --list --inventory {{path/to/inventory}}`

- Display the default inventory in YAML:

`ansible-inventory --list --yaml`

- Dump the default inventory to a file:

`ansible-inventory --list --output {{path/to/file}}`
