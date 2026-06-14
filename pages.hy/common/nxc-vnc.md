# nxc vnc

> Pentest և շահագործել VNC սերվերները:.
> Լրացուցիչ տեղեկություններ. <https://www.netexec.wiki/getting-started/selecting-and-using-a-protocol>:.

- Որոնեք վավեր հավատարմագրեր՝ փորձելով յուրաքանչյուր համակցություն օգտանունների և գաղտնաբառերի նշված ցուցակներում.:

`nxc vnc {{192.168.178.2}} {{[-u|--username]}} {{path/to/usernames.txt}} {{[-p|--password]}} {{path/to/passwords.txt}}`

- Խուսափեք տոկոսադրույքի սահմանափակումից VNC- քնի միջոցով.:

`nxc vnc {{192.168.178.2}} {{[-u|--username]}} {{path/to/usernames.txt}} {{[-p|--password]}} {{path/to/passwords.txt}} --vnc-sleep {{10}}`

- Վերցրեք սքրինշոթ հեռակառավարման համակարգում նշված ժամկետը սպասելուց հետո.:

`nxc vnc {{192.168.178.2}} {{[-u|--username]}} {{username}} {{[-p|--password]}} {{password}} --screenshot --screentime {{10}}`
