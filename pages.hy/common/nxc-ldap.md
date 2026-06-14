# nxc ldap

> Փորձարկել և շահագործել Windows Active Directory տիրույթները LDAP-ի միջոցով:.
> Լրացուցիչ տեղեկություններ. <https://www.netexec.wiki/ldap-protocol/authentication>:.

- Որոնեք վավեր տիրույթի հավատարմագրերը՝ փորձելով յուրաքանչյուր համակցություն օգտանունների և գաղտնաբառերի նշված ցուցակներում.:

`nxc ldap {{192.168.178.2}} {{[-u|--username]}} {{path/to/usernames.txt}} {{[-p|--password]}} {{path/to/passwords.txt}}`

- Թվարկեք ակտիվ տիրույթի օգտվողները.:

`nxc ldap {{192.168.178.2}} {{[-u|--username]}} {{username}} {{[-p|--password]}} {{password}} --active-users`

- Հավաքեք տվյալներ թիրախային տիրույթի մասին և ավտոմատ կերպով ներմուծեք այս տվյալները BloodHound.:

`nxc ldap {{192.168.178.2}} {{[-u|--username]}} {{username}} {{[-p|--password]}} {{password}} --bloodhound {{[-c|--collection]}} {{All}}`

- Փորձեք հավաքել AS_REP հաղորդագրություններ նշված օգտվողի համար՝ ASREPRoasting հարձակում իրականացնելու համար.:

`nxc ldap {{192.168.178.2}} {{[-u|--username]}} {{username}} {{[-p|--password]}} '' --asreproast {{path/to/output.txt}}`

- Փորձեք հանել տիրույթում խմբային կառավարվող ծառայության հաշիվների գաղտնաբառերը.:

`nxc ldap {{192.168.178.2}} {{[-u|--username]}} {{username}} {{[-p|--password]}} {{password}} --gmsa`
