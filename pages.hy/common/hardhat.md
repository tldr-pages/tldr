#ծանր գլխարկ

> Ethereum ծրագրաշարի զարգացման միջավայր:.
> Լրացուցիչ տեղեկություններ. <https://hardhat.org/hardhat-runner/docs/getting-started#quick-start>:.

- Ցուցակեք հասանելի ենթահրամանները (կամ ստեղծեք նոր նախագիծ, եթե կոնֆիգուրացիա չկա).:

`hardhat`

- Կազմեք ընթացիկ նախագիծը և կառուցեք բոլոր արտեֆակտները.:

`hardhat compile`

- Նախագիծը կազմելուց հետո գործարկեք օգտվողի կողմից սահմանված սկրիպտը.:

`hardhat run {{path/to/script.js}}`

- Գործարկել Mocha թեստերը.:

`hardhat test`

- Գործարկեք բոլոր տրված թեստային ֆայլերը.:

`hardhat test {{path/to/file1.js path/to/file2.js ...}}`

- Սկսեք տեղական Ethereum JSON-RPC հանգույց մշակման համար.:

`hardhat node`

- Սկսեք տեղական Ethereum JSON-RPC հանգույցը հատուկ հյուրընկալողի անունով և պորտով.:

`hardhat node --hostname {{hostname}} --port {{port}}`

- Մաքրել քեշը և բոլոր արտեֆակտները.:

`hardhat clean`
