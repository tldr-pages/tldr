# minifab

> Strumento per semplificare il settaggio e il deployment di una blockchain Hyperledger Fabric.
> Ulteriori informazioni: <https://github.com/hyperledger-labs/minifabric>.

- Crea la blockchain Hyperledger Fabric:

`minifab up -i {{minifab_version}}`

- Rimuovi la blockchain Hyperledger Fabric:

`minifab down`

- Installa smart contract su un canale:

`minifab install -n {{chaincode_name}}`

- Installa smart contract su un canale specificando la versione:

`minifab install -n {{chaincode_name}} -v {{chaincode_version}}`

- Inizializza smart contract dopo installazione/aggiornamento dello stesso:

`minifab approve,commit,initialize,discover`

- Interroga smart contract con argomenti:

`minifab invoke -n {{chaincode_name}} -p '"{{method_name}}", "{{arg0}}", "{{arg1}}", ...'`

- Interroga la blockchain:

`minifab blockquery {{block_number}}`

- Esegui direttamente l'applicazione:

`minifab apprun -l {{programming_langauge}}`