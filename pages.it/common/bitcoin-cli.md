# bitcoin-cli

> Client da linea di comando per interagire con il demone Bitcoin Core tramite chiamate RPC.
> Utilizza la configurazione definita in `bitcoin.conf`.
> Maggiori informazioni: <https://en.bitcoin.it/wiki/Running_Bitcoin#Command-line_arguments>.

- Invia una transazione a un dato indirizzo:

`bitcoin-cli sendtoaddress "{{indirizzo}}" {{importo}}`

- Genera uno o più blocchi:

`bitcoin-cli generate {{numero_blocchi}}`

- Mostra informazioni di alto livello sul portafoglio:

`bitcoin-cli getwalletinfo`

- Elenca tutti gli output di transazioni precedenti disponibili per finanziare nuove transazioni:

`bitcoin-cli listunspent`

- Esporta le informazioni del portafoglio in un file di testo:

`bitcoin-cli dumpwallet "{{percorso/del/file}}"`

- Ottieni informazioni sulla blockchain:

`bitcoin-cli getblockchaininfo`

- Ottieni informazioni sulla rete:

`bitcoin-cli getnetworkinfo`

- Ferma il demone Bitcoin Core:

`bitcoin-cli stop`
