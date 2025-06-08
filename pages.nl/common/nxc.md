# nxc

> Netwerk service opsomming en exploitatie gereedschap.
> Sommige subcommando's zoals `smb` hebben hun eigen gebruiksdocumentatie.
> Meer informatie: <https://www.netexec.wiki/getting-started/selecting-and-using-a-protocol>.

- Toon een lijst van beschikbare modules voor het opgegeven protocol:

`nxc {{smb|ssh|ldap|ftp|wmi|winrm|rdp|vnc|mssql}} {{[-L|--list-modules]}}`

- Toont de opties die beschikbaar zijn voor de opgegeven module:

`nxc {{smb|ssh|ldap|ftp|wmi|winrm|rdp|vnc|mssql}} {{[-M|--module]}} {{module_naam}} --options`

- Geef een [o]ptie op voor een module:

`nxc {{smb|ssh|ldap|ftp|wmi|winrm|rdp|vnc|mssql}} {{[-M|--module]}} {{module_naam}} -o {{OPTIE_NAAM}}={{optie_waarde}}`

- Bekijk de opties die beschikbaar zijn voor het opgegeven protocol:

`nxc {{smb|ssh|ldap|ftp|wmi|winrm|rdp|vnc|mssql}} {{[-h|--help]}}`
