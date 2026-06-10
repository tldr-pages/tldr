#Ջոն

> Գաղտնաբառի կոտրիչ:.
> Լրացուցիչ տեղեկություններ. <https://www.openwall.com/john/>:.

- կոտրել գաղտնաբառի հեշերը.:

`john {{path/to/hashes.txt}}`

- Ցույց տալ կոտրված գաղտնաբառերը.:

`john --show {{path/to/hashes.txt}}`

- Ցուցադրել օգտվողների կոտրված գաղտնաբառերը օգտվողի նույնացուցիչով բազմաթիվ ֆայլերից.:

`john --show --users={{user_ids}} {{path/to/hashes1.txt path/to/hashes2.txt ...}}`

- Կոտրեք գաղտնաբառի հեշերը՝ օգտագործելով հատուկ բառացանկ.:

`john --wordlist={{path/to/wordlist.txt}} {{path/to/hashes.txt}}`

- Ցուցակեք հասանելի հեշ ձևաչափերը.:

`john --list=formats`

- Կոտրեք գաղտնաբառի հեշերը՝ օգտագործելով հատուկ հեշ ձևաչափ.:

`john --format={{md5crypt}} {{path/to/hashes.txt}}`

- Կոտրեք գաղտնաբառի հեշերը՝ միացնելով բառերի խեղաթյուրման կանոնները.:

`john --rules {{path/to/hashes.txt}}`

- Վերականգնել ընդհատված cracking նիստը պետական ֆայլից, օրինակ. `mycrack.rec`:

`john --restore={{path/to/mycrack.rec}}`
