# nxc winrm

> Pentest եւ շահագործել Windows Remote Management (winrm):.
> Լրացուցիչ տեղեկություններ. <https://www.netexec.wiki/winrm-protocol/password-spraying>:.

- Որոնեք վավեր հավատարմագրեր՝ փորձելով յուրաքանչյուր համակցություն օգտանունների և գաղտնաբառերի նշված ցուցակներում.:

`nxc winrm {{192.168.178.2}} {{[-u|--username]}} {{path/to/usernames.txt}} {{[-p|--password]}} {{path/to/passwords.txt}}`

- Նշեք նույնականացման տիրույթը (խուսափում է նախնական SMB կապից).:

`nxc winrm {{192.168.178.2}} {{[-u|--username]}} {{username}} {{[-p|--password]}} {{password}} -d {{domain_name}}`

- Կատարեք նշված հրամանը հոսթի վրա.:

`nxc winrm {{192.168.178.2}} {{[-u|--username]}} {{username}} {{[-p|--password]}} {{password}} -x {{whoami}}`

- Կատարեք նշված PowerShell հրամանը հոսթի վրա որպես ադմինիստրատոր՝ օգտագործելով LAPS:

`nxc winrm {{192.168.178.2}} {{[-u|--username]}} {{username}} {{[-p|--password]}} {{password}} --laps -X {{whoami}}`
