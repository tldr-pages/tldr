# semodule

> Manage SELinux policy modules.
> See also: `audit2allow`, `semanage`.
> More information: <https://manned.org/semodule>.

- List all installed policy modules:

`sudo semodule -l`

- Install a new policy module:

`sudo semodule -i {{path/to/module.pp}}`

- Remove a policy module:

`sudo semodule -r {{module_name}}`

- Enable a policy module:

`sudo semodule -e {{module_name}}`

- Disable a policy module:

`sudo semodule -d {{module_name}}`

- Reload all policy modules:

`sudo semodule -R`

- Display the version of installed policy modules:

`sudo semodule -l -v`
