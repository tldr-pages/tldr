# sui հաճախորդ

> Հրապարակեք խելացի պայմանագրեր, ստացեք օբյեկտների մասին տեղեկատվություն, կատարեք գործարքներ և այլն:.
> Լրացուցիչ տեղեկություններ. <https://docs.sui.io/references/cli/client>:.

- Ստեղծեք նոր հասցե ED25519 սխեմայով.:

`sui client new-address ed25519 {{address-alias}}`

- Ստեղծեք նոր testnet միջավայր RPC URL-ով և կեղծանունով.:

`sui client new-env --rpc https://fullnode.testnet.sui.io:443 --alias testnet`

- Անցեք ձեր ընտրած հասցեին (ընդունում է նաև կեղծանունը).:

`sui client switch --address {{address-alias}}`

- Անցում տվյալ միջավայրին.:

`sui client switch --env {{env-alias}}`

- Հրապարակեք խելացի պայմանագիր.:

`sui client publish {{package-path}}`

- Փոխազդեք Sui ծորակի հետ.:

`sui client faucet {{subcommand}}`

- Թվարկեք գազի մետաղադրամները տվյալ հասցեի համար (ընդունում է նաև կեղծանունը).:

`sui client gas {{address}}`

- Ստեղծեք, ստորագրեք և կատարեք ծրագրավորվող գործարքների բլոկներ.:

`sui client ptb {{options}} {{subcommand}}`
