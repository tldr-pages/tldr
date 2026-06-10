# nxc wmi

> Փորձարկեք և օգտագործեք Windows կառավարման գործիքավորումը (WMI):.
> Լրացուցիչ տեղեկություններ. <https://www.netexec.wiki/wmi-protocol/password-spraying>:.

- Որոնեք վավեր հավատարմագրեր՝ փորձելով յուրաքանչյուր համակցություն օգտանունների և գաղտնաբառերի նշված ցուցակներում.:

`nxc wmi {{192.168.178.2}} {{[-u|--username]}} {{path/to/usernames.txt}} {{[-p|--password]}} {{path/to/passwords.txt}}`

- Նույնականացում տեղական նույնականացման միջոցով (ի տարբերություն տիրույթի նույնականացման).:

`nxc wmi {{192.168.178.2}} {{[-u|--username]}} {{username}} {{[-p|--password]}} {{password}} --local-auth`

- Թողարկեք նշված WMI հարցումը.:

`nxc wmi {{192.168.178.2}} {{[-u|--username]}} {{username}} {{[-p|--password]}} {{password}} --wmi {{wmi_query}}`

- Կատարեք նշված հրամանը թիրախավորված հոսթի վրա.:

`nxc wmi {{192.168.178.2}} {{[-u|--username]}} {{username}} {{[-p|--password]}} {{password}} -x {{command}}`
