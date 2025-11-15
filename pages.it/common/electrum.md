# electrum

> Ergonomico wallet (portafogli) Bitcoin e gestore di chiavi private.
> Maggiori informazioni: <https://electrum.org>.

- Crea un nuovo wallet:

`electrum -w {{nuovo_wallet.dat}} create`

- Ripristina un wallet esistente da un seed offline:

`electrum -w {{wallet_ripristinato.dat}} restore -o`

- Crea una transazione firmata offline:

`electrum mktx {{destinatario}} {{ammontare}} -f 0.0000001 -F {{mittente}} -o`

- Mostra tutti gli indirizzi del wallet per la ricezione:

`electrum listaddresses -a`

- Firma un messaggio:

`electrum signmessage {{indirizzo}} {{messaggio}}`

- Verifica un messaggio:

`electrum verifymessage {{indirizzo}} {{firma}} {{messaggio}}`

- Connettiti solo ad una specifica istanza electrum-server:

`electrum -p socks5:{{127.0.0.1}}:9050 -s {{56ckl5obj37gypcu.onion}}:50001:t -1`
