# nxc mssql

> Փորձարկել և շահագործել Microsoft SQL սերվերները:.
> Լրացուցիչ տեղեկություններ. <https://www.netexec.wiki/mssql-protocol/mssql-passwordspray>:.

- Որոնեք վավեր հավատարմագրեր՝ փորձելով յուրաքանչյուր համակցություն օգտանունների և գաղտնաբառերի նշված ցուցակներում.:

`nxc mssql {{192.168.178.2}} {{[-u|--username]}} {{path/to/usernames.txt}} {{[-p|--password]}} {{path/to/passwords.txt}}`

- Կատարեք նշված SQL հարցումը թիրախային սերվերի վրա.:

`nxc mssql {{192.168.178.2}} {{[-u|--username]}} {{username}} {{[-p|--password]}} {{password}} {{[-q|--query]}} '{{SELECT * FROM sys.databases;}}'`

- Կատարեք նշված shell հրամանը թիրախային սերվերի վրա MSSQL-ի միջոցով.:

`nxc mssql {{192.168.178.2}} {{[-u|--username]}} {{username}} {{[-p|--password]}} {{password}} -x {{whoami}}`

- Կատարեք նշված PowerShell հրամանը թիրախային սերվերի վրա MSSQL-ի միջոցով՝ առանց ելք վերցնելու.:

`nxc mssql {{192.168.178.2}} {{[-u|--username]}} {{username}} {{[-p|--password]}} {{password}} -X {{whoami}} --no-output`

- Ներբեռնեք հեռակա ֆայլ թիրախային սերվերից և պահեք այն նշված վայրում.:

`nxc mssql {{192.168.178.2}} {{[-u|--username]}} {{username}} {{[-p|--password]}} {{password}} --get-file {{C:\path\to\remote_file}} {{path/to/local_file}}`

- Վերբեռնեք տեղական ֆայլ թիրախային սերվերի նշված վայրում.:

`nxc mssql {{192.168.178.2}} {{[-u|--username]}} {{username}} {{[-p|--password]}} {{password}} --put-file {{path/to/local_file}} {{C:\path\to\remote_file}}`
