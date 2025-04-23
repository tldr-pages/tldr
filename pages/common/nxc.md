# nxc

> Network service enumeration and exploitation tool.
> Some subcommands such as `smb` have their own usage documentation.
> More information: <https://www.netexec.wiki/getting-started/selecting-and-using-a-protocol>.

- [L]ist available modules for the specified protocol:

`nxc {{smb|ssh|ldap|ftp|wmi|winrm|rdp|vnc|mssql}} -L`

- List the options available for the specified module:

`nxc {{smb|ssh|ldap|ftp|wmi|winrm|rdp|vnc|mssql}} -M {{module_name}} --options`

- Specify an option for a module:

`nxc {{smb|ssh|ldap|ftp|wmi|winrm|rdp|vnc|mssql}} -M {{module_name}} -o {{OPTION_NAME}}={{option_value}}`

- View the options available for the specified protocol:

`nxc {{smb|ssh|ldap|ftp|wmi|winrm|rdp|vnc|mssql}} --help`
