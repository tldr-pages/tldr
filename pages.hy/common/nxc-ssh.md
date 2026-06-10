# nxc ssh

> Pentest և շահագործել SSH սերվերները:.
> Տես նաև՝ `hydra`:.
> Լրացուցիչ տեղեկություններ. <https://www.netexec.wiki/ssh-protocol/password-spraying>:.

- Նշված գաղտնաբառը ցողեք նշված թիրախի վրա օգտագործողների անունների ցանկի վրա.:

`nxc ssh {{192.168.178.2}} {{[-u|--username]}} {{path/to/usernames.txt}} {{[-p|--password]}} {{password}}`

- Որոնեք վավեր հավատարմագրեր՝ փորձելով յուրաքանչյուր համակցություն օգտանունների և գաղտնաբառերի նշված ցուցակներում.:

`nxc ssh {{192.168.178.2}} {{[-u|--username]}} {{path/to/usernames.txt}} {{[-p|--password]}} {{path/to/passwords.txt}}`

- Նույնականացման համար օգտագործեք նշված անձնական բանալին՝ որպես բանալու անցաբառ օգտագործելով տրամադրված գաղտնաբառը.:

`nxc ssh {{192.186.178.2}} {{[-u|--username]}} {{path/to/usernames.txt}} {{[-p|--password]}} {{password}} --key-file {{path/to/id_rsa}}`

- Փորձեք օգտվողի անվան և գաղտնաբառի համադրություն մի շարք թիրախների վրա.:

`nxc ssh {{192.168.178.0/24}} {{[-u|--username]}} {{username}} {{[-p|--password]}} {{password}}`

- Հաջող մուտքի դեպքում ստուգեք `sudo` արտոնությունները.:

`nxc ssh {{192.168.178.2}} {{[-u|--username]}} {{username}} {{[-p|--password]}} {{path/to/passwords.txt}} --sudo-check`
