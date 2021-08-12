# minifab

> Instrument utilitar care automatizează configurarea și implementarea rețelelor Hyperledger Fabric.
> Mai multe informaţii: <https://github.com/hyperledger-labs/minifabric>

- Aduceți rețeaua implicită Hyperledger Fabric:

`minifab up -i {{minifab_version}}`

- Aduce în jos rețeaua Hyperledger Fabric:

`minifab down`

- Instalați chaincode pe un canal specificat:

`minifab install -n {{chaincode_name}}`

- Instalați o versiune specifică a chaincode pe un canal:

`minifab install -n {{chaincode_name}} -v {{chaincode_version}}`

- Initializati chaincode dupa instalare/upgrade:

`minifab approve,commit,initialize,discover`

- Invocați o metodă chaincode cu argumentele specificate:

`minifab invoke -n {{chaincode_name}} -p '"{{method_name}}", "{{arg0}}", "{{arg1}}", ...'`

- Faceți o interogare în registru:

`minifab blockquery {{block_number}}`

- Rulați rapid o aplicație:

`minifab apprun -l {{app_programming_langauge}}`
