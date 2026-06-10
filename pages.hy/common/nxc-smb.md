# nxc smb

> Pentest և շահագործել SMB սերվերները:.
> Լրացուցիչ տեղեկություններ. <https://www.netexec.wiki/smb-protocol/generate-hosts-file>:.

- Որոնեք վավեր տիրույթի հավատարմագրերը՝ փորձելով յուրաքանչյուր համակցություն օգտանունների և գաղտնաբառերի նշված ցուցակներում.:

`nxc smb {{192.168.178.2}} {{[-u|--username]}} {{path/to/usernames.txt}} {{[-p|--password]}} {{path/to/passwords.txt}}`

- Որոնեք վավեր հավատարմագրեր տեղական հաշիվների համար՝ տիրույթի հաշիվների փոխարեն.:

`nxc smb {{192.168.178.2}} {{[-u|--username]}} {{path/to/usernames.txt}} {{[-p|--password]}} {{path/to/passwords.txt}} --local-auth`

- Թվարկեք SMB-ի բաժնետոմսերը և նշված օգտատերերի մուտքի իրավունքները թիրախային հոսթերներում.:

`nxc smb {{192.168.178.0/24}} {{[-u|--username]}} {{username}} {{[-p|--password]}} {{password}} --shares`

- Թվարկեք ցանցային ինտերֆեյսները թիրախային հոսթերների վրա՝ կատարելով նույնականացում pass-the-hash-ի միջոցով.:

`nxc smb {{192.168.178.30-45}} {{[-u|--username]}} {{username}} {{[-H|--hash]}} {{NTLM_hash}} --interfaces`

- Սկանավորեք թիրախային հյուրընկալող սարքերը ընդհանուր խոցելիության համար.:

`nxc smb {{path/to/target_list.txt}} {{[-u|--username]}} '' {{[-p|--password]}} '' {{[-M|--module]}} zerologon {{[-M|--module]}} petitpotam`

- Փորձեք հրաման կատարել թիրախային հոսթերների վրա.:

`nxc smb {{192.168.178.2}} {{[-u|--username]}} {{username}} {{[-p|--password]}} {{password}} -x {{command}}`
