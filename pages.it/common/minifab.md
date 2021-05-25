# minifab

> Strumento per semplificare il settaggio e il deployment di una blockchain Hyperledger Fabric.
> Maggiori informazioni: <https://github.com/hyperledger-labs/minifabric>.

- Crea la blockchain Hyperledger Fabric:

`minifab up -i {{versione_minifab}}`

- Rimuovi la blockchain Hyperledger Fabric:

`minifab down`

- Installa smart contract su un canale:

`minifab install -n {{nome_smart_contract}}`

- Installa smart contract su un canale specificando la versione:

`minifab install -n {{nome_smart_contract}} -v {{versione_smart_contract}}`

- Inizializza smart contract dopo installazione/aggiornamento dello stesso:

`minifab approve,commit,initialize,discover`

- Interroga smart contract con argomenti:

`minifab invoke -n {{nome_smart_contract}} -p '"{{nome_metodo}}", "{{arg0}}", "{{arg1}}", ...'`

- Interroga la blockchain:

`minifab blockquery {{numero_blocco}}`

- Esegui direttamente l'applicazione:

`minifab apprun -l {{linguaggio_di_programmazione}}`
