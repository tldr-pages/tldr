# nxc

> Herramienta de enumeración y explotación de servicios de red.
> Algunos subcomandos como `smb` tienen su propia documentación de uso.
> Más información: <https://www.netexec.wiki/getting-started/selecting-and-using-a-protocol>.

- Lista módulos disponibles para el protocolo especificado:

`nxc {{smb|ssh|ldap|ftp|wmi|winrm|rdp|vnc|mssql}} {{[-L|--list-modules]}}`

- Lista las opciones disponibles para el módulo especificado:

`nxc {{smb|ssh|ldap|ftp|wmi|winrm|rdp|vnc|mssql}} {{[-M|--module]}} {{nombre_del_módulo}} --options`

- Especifica una opción para un módulo:

`nxc {{smb|ssh|ldap|ftp|wmi|winrm|rdp|vnc|mssql}} {{[-M|--module]}} {{nombre_del_módulo}} -o {{NOMBRE_OPCION}}={{valor_opción}}`

- Vea las opciones disponibles para el protocolo especificado:

`nxc {{smb|ssh|ldap|ftp|wmi|winrm|rdp|vnc|mssql}} {{[-h|--help]}}`
