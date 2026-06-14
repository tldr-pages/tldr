# nxc

> Ցանցային ծառայության թվարկման և շահագործման գործիք:.
> Որոշ ենթահրամաններ, ինչպիսիք են `smb`-ն, ունեն իրենց օգտագործման փաստաթղթերը:.
> Լրացուցիչ տեղեկություններ. <https://www.netexec.wiki/getting-started/selecting-and-using-a-protocol>:.

- Նշեք նշված արձանագրության համար հասանելի մոդուլները.:

`nxc {{smb|ssh|ldap|ftp|wmi|winrm|rdp|vnc|mssql}} {{[-L|--list-modules]}}`

- Նշեք նշված մոդուլի համար մատչելի տարբերակները.:

`nxc {{smb|ssh|ldap|ftp|wmi|winrm|rdp|vnc|mssql}} {{[-M|--module]}} {{module_name}} --options`

- Նշեք [o]տարբերակ մոդուլի համար.:

`nxc {{smb|ssh|ldap|ftp|wmi|winrm|rdp|vnc|mssql}} {{[-M|--module]}} {{module_name}} -o {{OPTION_NAME}}={{option_value}}`

- Դիտեք նշված արձանագրության համար հասանելի ընտրանքները.:

`nxc {{smb|ssh|ldap|ftp|wmi|winrm|rdp|vnc|mssql}} {{[-h|--help]}}`
