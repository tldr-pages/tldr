#էլեկտրում

> Էրգոնոմիկ Bitcoin դրամապանակ և մասնավոր բանալիների կառավարում:.
> Լրացուցիչ տեղեկություններ. <https://manned.org/electrum>:.

- Ստեղծեք նոր դրամապանակ.:

`electrum {{[-w|--wallet]}} {{path/to/new_wallet.dat}} create`

- Վերականգնել գոյություն ունեցող դրամապանակը սերմից անցանց.:

`electrum {{[-w|--wallet]}} {{path/to/recovery_wallet.dat}} restore {{[-o|--offline]}}`

- Ստեղծեք ստորագրված գործարք անցանց.:

`electrum mktx {{recipient}} {{amount}} {{[-f|--fee]}} 0.0000001 {{[-F|--from-addr]}} {{from}} {{[-o|--offline]}}`

- Ցուցադրել դրամապանակի ստացման բոլոր հասցեները.:

`electrum listaddresses -a`

- Ստորագրեք հաղորդագրություն.:

`electrum signmessage {{address}} {{message}}`

- Ստուգեք հաղորդագրությունը.:

`electrum verifymessage {{address}} {{signature}} {{message}}`

- Միացեք միայն հատուկ էլեկտրական սերվերի օրինակին.:

`electrum {{[-p|--proxy]}} socks5:{{127.0.0.1}}:9050 {{[-s|--server]}} {{56ckl5obj37gypcu.onion}}:50001:t {{[-1|--oneserver]}}`
