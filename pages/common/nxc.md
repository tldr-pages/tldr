# nxc

> Network service enumeration and exploitation tool.
> Some subcommands such as `smb` have their own usage documentation.
> More information: <https://www.netexec.wiki/getting-started/selecting-and-using-a-protocol>.

- List available modules for the specified protocol:

`nxc {{smb|ssh|ldap|ftp|wmi|winrm|rdp|vnc|mssql}} {{[-L|--list-modules]}}`

- List the options available for the specified module:

`nxc {{smb|ssh|ldap|ftp|wmi|winrm|rdp|vnc|mssql}} {{[-M|--module]}} {{module_name}} --options`

- Specify an [o]ption for a module:

`nxc {{smb|ssh|ldap|ftp|wmi|winrm|rdp|vnc|mssql}} {{[-M|--module]}} {{module_name}} -o {{OPTION_NAME}}={{option_value}}`

- View the options available for the specified protocol:

`nxc {{smb|ssh|ldap|ftp|wmi|winrm|rdp|vnc|mssql}} {{[-h|--help]}}`
