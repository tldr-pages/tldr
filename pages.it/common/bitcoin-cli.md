# bitcoin-cli

> Client da linea di comando per interagire con il demone Bitcoin tramite chiamate RPC.
> Utilizza la configurazione definita in `bitcoin.conf`.
> Maggiori informazioni: <https://en.bitcoin.it/wiki/Running_Bitcoin#Command-line_arguments>.

- Invia una transazione ad un dato indirizzo:

`bitcoin-cli sendtoaddress "{{indirizzo}}" {{importo}}`

- Genera uno o più blocchi:

`bitcoin-cli generate {{numero_blocchi}}`

- Mostra informazioni di alto livello sul portafogli:

`bitcoin-cli getwalletinfo`

- Elenca tutti gli output di transazioni precedenti disponibili per finanziare una nuove transazioni:

`bitcoin-cli listunspent`

- Esporta le informazioni sul portafogli in un file di testo:

`bitcoin-cli dumpwallet "{{percorso/del/file}}"`
