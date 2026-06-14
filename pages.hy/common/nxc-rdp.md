# nxc rdp

> Pentest և շահագործել RDP սերվերները:.
> Լրացուցիչ տեղեկություններ. <https://www.netexec.wiki/rdp-protocol/password-spraying>:.

- Որոնեք վավեր հավատարմագրեր՝ փորձելով յուրաքանչյուր համակցություն օգտանունների և գաղտնաբառերի նշված ցուցակներում.:

`nxc rdp {{192.168.178.2}} {{[-u|--username]}} {{path/to/usernames.txt}} {{[-p|--password]}} {{path/to/passwords.txt}}`

- Վերցրեք սքրինշոթ՝ նշված թվով վայրկյան սպասելուց հետո.:

`nxc rdp {{192.168.178.2}} {{[-u|--username]}} {{username}} {{[-p|--password]}} {{password}} --screenshot --screentime {{10}}`

- Վերցրեք սքրինշոթ նշված լուծաչափով.:

`nxc rdp {{192.168.178.2}} {{[-u|--username]}} {{username}} {{[-p|--password]}} {{password}} --screenshot --res {{1024x768}}`

- Վերցրեք RDP մուտքի հուշման սքրինշոթը, եթե ցանցի մակարդակի նույնականացումը անջատված է.:

`nxc rdp {{192.168.178.2}} {{[-u|--username]}} {{username}} {{[-p|--password]}} {{password}} --nla-screenshot`
