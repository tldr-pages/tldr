# minifab

> Utility tool that automates the setup and deployment of Hyperledger Fabric networks.
> More information: <https://github.com/hyperledger-labs/minifabric>.

- Bring up default Hyperledger Fabric network:

`minifab up -i {{minifab_version}}`

- Bring down Hyperldger Fabric network:

`minifab down`

- Install chaincode onto channel:

`minifab install -n {{chaincode_name}}`

- Install chaincode version onto channel:

`minifab install -n {{chaincode_name}} -v {{chaincode_version}}`

- Initialize chaincode after installation/upgrade:

`minifab approve,commit,initialize,discover`

- Invoke a chaincode method with args:

`minifab invoke -n {{chaincode_name}} -p '"{{method_name}}", "{{arg0}}", "{{arg1}}", ...'`

- Make a query on the ledger:

`minifab blockquery {{block_number}}`

- Quickly run application:

`minifab apprun -l {{app_programming_langauge}}`
