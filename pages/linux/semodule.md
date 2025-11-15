# semodule

> Manage SELinux policy modules.
> See also: `audit2allow`, `semanage`.
> More information: <https://manned.org/semodule>.

- List all installed policy modules:

`sudo semodule {{[-l|--list]}}`

- Install a new policy module:

`sudo semodule {{[-i|--install]}} {{path/to/module.pp}}`

- Remove a policy module:

`sudo semodule {{[-r|--remove]}} {{module_name}}`

- Enable a policy module:

`sudo semodule {{[-e|--enable]}} {{module_name}}`

- Disable a policy module:

`sudo semodule {{[-d|--disable]}} {{module_name}}`

- Reload all policy modules:

`sudo semodule {{[-R|--reload]}}`

- Display the version of installed policy modules:

`sudo semodule {{[-l|--list]}} {{[-v|--verbose]}}`
