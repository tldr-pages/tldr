# nping

> Ցանցային փաթեթների ստեղծման գործիք/ping կոմունալ:.
> Լրացուցիչ տեղեկություններ. <https://nmap.org/nping/>:.

- Ping նշված հոսթին օգտագործելով ICMP, եթե օգտվողին թույլատրված է, այլապես օգտագործելով TCP:

`nping {{example.com}}`

- Ping նշված հոսթինգը՝ օգտագործելով ICMP՝ ենթադրելով, որ օգտվողին թույլատրվում է դա անել.:

`nping --icmp --privileged {{example.com}}`

- Ping նշված հոսթին օգտագործելով UDP:

`nping --udp {{example.com}}`

- Ping նշված հոսթին տվյալ նավահանգստում՝ օգտագործելով TCP:

`nping --tcp --dest-port {{443}} {{example.com}}`

- Ping որոշակի քանակությամբ անգամներ.:

`nping --count {{10}} {{example.com}}`

- Յուրաքանչյուր պինգի միջև որոշակի ժամանակ սպասեք.:

`nping --delay {{5s}} {{example.com}}`

- Ուղարկեք հարցումը նշված ինտերֆեյսի միջոցով.:

`nping --interface {{eth0}} {{example.com}}`

- Ping IP տիրույթ.:

`nping {{10.0.0.1-10}}`
