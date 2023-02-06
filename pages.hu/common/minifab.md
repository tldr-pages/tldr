# minifab

> A Hyperledger Fabric hálózatok beállítását és telepítését automatizáló segédeszköz. További információ: <https://github.com/hyperledger-labs/minifabric>.

- Hozzuk létre az alapértelmezett Hyperledger Fabric hálózatot:

`minifab up -i {{minifab_version}}`

- A Hyperledger Fabric hálózat leállítása:

`minifab down`

- Telepítse a chaincode-ot egy megadott csatornára:

`minifab install -n {{chaincode_name}}`

- Egy adott chaincode-verzió telepítése egy csatornára:

`minifab install -n {{chaincode_name}} -v {{chaincode_version}}`

- A chaincode inicializálása telepítés/frissítés után:

`minifab approve,commit,initialize,discover`

- Chaincode metódus meghívása a megadott argumentumokkal:

`minifab invoke -n {{chaincode_name}} -p '"{{method_name}}", "{{arg0}}", "{{arg1}}", ...'`

- Lekérdezés végrehajtása a főkönyvben:

`minifab blockquery {{block_number}}`

- Egy alkalmazás gyors futtatása:

`minifab apprun -l {{app_programming_langauge}}`
