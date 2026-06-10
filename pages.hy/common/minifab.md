# մինիֆաբոր

> Ավտոմատացրեք Hyperledger Fabric ցանցերի կարգավորումն ու տեղակայումը:.
> Լրացուցիչ տեղեկություններ. <https://github.com/hyperledger-labs/minifabric>:.

- Բերեք լռելյայն Hyperledger Fabric ցանցը.:

`minifab up {{[-i|--fabric-release]}} {{minifab_version}}`

- Անջատեք Hyperledger Fabric ցանցը.:

`minifab down`

- Տեղադրեք շղթայական կոդը նշված ալիքի վրա.:

`minifab install {{[-n|--chaincode-name]}} {{chaincode_name}}`

- Տեղադրեք շղթայական կոդի հատուկ տարբերակ ալիքի վրա.:

`minifab install {{[-n|--chaincode-name]}} {{chaincode_name}} {{[-v|--chaincode-version]}} {{chaincode_version}}`

- Նախաձեռնեք շղթայի կոդը տեղադրումից/թարմացումից հետո.:

`minifab approve,commit,initialize,discover`

- Կանչեք շղթայական կոդի մեթոդ նշված արգումենտներով.:

`minifab invoke {{[-n|--chaincode-name]}} {{chaincode_name}} {{[-p|--chaincode-parameters]}} '"{{method_name}}", {{"argument1", "argument2", ...}}'`

- Հարցում կատարեք մատյանում.:

`minifab blockquery {{block_number}}`

- Արագ գործարկեք հավելվածը.:

`minifab apprun {{[-l|--chaincode-language]}} {{app_programming_language}}`
