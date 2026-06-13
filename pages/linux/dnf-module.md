# dnf module

> Manage package modularity.
> More information: <https://dnf.readthedocs.io/en/latest/command_ref.html#module-command>.

- View the modularity overview:

`dnf module list`

- View modularity of a specific program:

`dnf module list {{package_name}}`

- Set a package to be enabled:

`sudo dnf module enable {{package_name}}:{{stream}}`

- Enable and install a specific version:

`dnf module install {{package_name}}:{{stream}}`
