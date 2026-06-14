# zmap

> Արագ, բաց կոդով ցանցային սկաներ՝ ամբողջ ինտերնետով հարցումների համար:.
> Տես նաև՝ `hping3`, `masscan`, `naabu`, `nmap`, `rustscan`:.
> Լրացուցիչ տեղեկություններ. <https://manned.org/zmap>:.

- Սկանավորեք ենթացանցը կամ ամբողջական IPv4 տարածքը որոշակի TCP պորտի համար (կանխադրված՝ 80):

`sudo zmap {{[-p|--target-ports]}} {{port}} {{subnet}}`

- Սկանավորեք որոշակի նավահանգիստներ կամ նավահանգիստների միջակայքերը ենթացանցում.:

`sudo zmap {{[-p|--target-ports]}} {{port1,port2-port3,...}} {{subnet}}`

- Արդյունքները թողարկեք CSV ֆայլ՝ հատուկ դաշտերով.:

`sudo zmap {{[-o|--output-file]}} {{path/to/output_file.csv}} {{[-f|--output-fields]}} "{{saddr,daddr,sport,dport}}" {{subnet}}`

- Սահմանափակեք սկանավորման արագությունը վայրկյանում փաթեթների որոշակի քանակով.:

`sudo zmap {{[-r|--rate]}} {{packets_per_second}} {{subnet}}`

- Կատարեք չոր վազք՝ առանց փաթեթներ ուղարկելու.:

`zmap {{[-d|--dryrun]}} {{subnet}}`

- Բացառեք ենթացանցերը՝ օգտագործելով բլոկ ցուցակի ֆայլը CIDR նշումով.:

`sudo zmap {{[-b|--blocklist-file]}} {{path/to/blocklist.txt}} {{subnet}}`

- Սահմանեք հատուկ աղբյուրի IP փաթեթների սկանավորման համար.:

`sudo zmap {{[-S|--source-ip]}} {{source_ip}} {{subnet}}`

- Սահմանափակեք հետազոտման ենթակա թիրախների քանակը/տոկոսը (օրինակ՝ 1000 IP/պորտ զույգ).:

`sudo zmap {{[-p|--target-ports]}} {{port1,port2-port3}} {{[-n|--max-targets]}} {{1000}} {{subnet}}`
