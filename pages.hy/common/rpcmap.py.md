# rpcmap.py

> Փնտրեք լսող MSRPC միջերեսները՝ օգտագործելով տողերի կապակցում (օրինակ՝ `ncacn_ip_tcp:host[port]`):.
> Impacket փաթեթի մի մասը:.
> Լրացուցիչ տեղեկություններ. <https://github.com/fortra/impacket>:.

- Միացեք MSRPC ինտերֆեյսին՝ օգտագործելով լարային կապ (օրինակ՝ `ncacn_ip_tcp:host[port]`):

`rpcmap.py {{stringbinding}}`

- Bruteforce UUID-ներ, նույնիսկ եթե MGMT ինտերֆեյսը հասանելի է.:

`rpcmap.py -brute-uuids {{stringbinding}}`

- Bruteforce գործողության համարները (opnums) հայտնաբերված UUID-ների համար.:

`rpcmap.py -brute-opnums {{stringbinding}}`

- Գտնված UUID-ների Bruteforce հիմնական տարբերակները.:

`rpcmap.py -brute-versions {{stringbinding}}`

- Ձեռքով նշեք թիրախային IP հասցեն.:

`rpcmap.py -target-ip {{ip_address}} {{stringbinding}}`

- Նույնականացրեք RPC ինտերֆեյսին օգտանունով և գաղտնաբառով.:

`rpcmap.py -auth-rpc {{domain}}/{{username}}:{{password}} {{stringbinding}}`

- Նույնականացրեք՝ օգտագործելով NTLM հեշերը RPC-ի համար.:

`rpcmap.py -hashes-rpc {{LMHASH:NTHASH}} {{stringbinding}}`

- Միացնել վրիպազերծման ելքը՝ մանրամասն տեղեկատվության համար.:

`rpcmap.py -debug {{stringbinding}}`
