# electrum

> Portofel ergonomic Bitcoin și gestionarea cheilor private.
> Mai multe informaţii: <https://electrum.org>

- Creați un portofel nou:

`electrum -w {{new_wallet.dat}} create`

- Restaurați un portofel existent din semințe offline:

`electrum -w {{recovery_wallet.dat}} restore -o`

- Creați o tranzacție semnată offline:

`electrum mktx {{recipient}} {{amount}} -f 0.0000001 -F {{from}} -o`

- Afișează toate adresele de primire portofel:

`electrum listaddresses -a`

- Semnează un mesaj:

`electrum signmessage {{address}} {{message}}`

- Verificarea unui mesaj:

`electrum verifymessage {{address}} {{signature}} {{message}}`

- Conectează-te numai la o anumită instanță de server electric:

`electrum -p socks5:{{127.0.0.1}}:9050 -s {{56ckl5obj37gypcu.onion}}:50001:t -1`
