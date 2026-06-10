# rpcdump.py

> Թափել հեռավոր RPC վերջնակետերի տեղեկատվությունը Endpoint Mapper-ի միջոցով:.
> Impacket փաթեթի մի մասը:.
> Լրացուցիչ տեղեկություններ. <https://github.com/fortra/impacket>:.

- Թափել RPC վերջնակետերը՝ օգտագործելով օգտվողի անունը և գաղտնաբառը.:

`rpcdump.py {{domain}}/{{username}}:{{password}}@{{target}}`

- Թափել RPC վերջնակետերը՝ օգտագործելով NTLM հեշերը.:

`rpcdump.py -hashes {{LMHASH}}:{{NTHASH}} {{domain}}/{{username}}:{{password}}@{{target}}`

- Հստակորեն նշեք թիրախային IP հասցեն (օգտակար է, եթե թիրախի անունը NetBIOS անուն է).:

`rpcdump.py -target-ip {{target_ip}} {{domain}}/{{username}}:{{password}}@{{target}}`

- Միացեք որոշակի նավահանգիստին (RPC Endpoint Mapper-ի համար կանխադրվածը 135 է).:

`rpcdump.py -port {{port_number}} {{domain}}/{{username}}:{{password}}@{{target}}`

- Միացնել վրիպազերծման ելքը.:

`rpcdump.py -debug {{domain}}/{{username}}:{{password}}@{{target}}`
