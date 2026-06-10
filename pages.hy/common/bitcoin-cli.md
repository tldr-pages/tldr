# bitcoin-cli

> Հաճախորդ՝ RPC զանգերի միջոցով Bitcoin Core դեմոնի հետ փոխազդելու համար:.
> Օգտագործում է `bitcoin.conf`-ում սահմանված կոնֆիգուրացիան:.
> Լրացուցիչ տեղեկություններ. <https://en.bitcoin.it/wiki/Running_Bitcoin#Command-line_arguments>:.

- Գործարք ուղարկել տվյալ հասցեով.:

`bitcoin-cli sendtoaddress "{{address}}" {{amount}}`

- Ստեղծեք մեկ կամ ավելի բլոկներ.:

`bitcoin-cli generate {{num_blocks}}`

- Տպեք բարձր մակարդակի տեղեկատվություն դրամապանակի մասին.:

`bitcoin-cli getwalletinfo`

- Թվարկեք բոլոր ելքերը նախորդ գործարքներից, որոնք հասանելի են ելքային գործարքները ֆինանսավորելու համար.:

`bitcoin-cli listunspent`

- Արտահանել դրամապանակի տեղեկատվությունը տեքստային ֆայլ.:

`bitcoin-cli dumpwallet "{{path/to/file}}"`

- Ստացեք բլոկչեյնի մասին տեղեկատվություն.:

`bitcoin-cli getblockchaininfo`

- Ստացեք ցանցի տեղեկատվություն.:

`bitcoin-cli getnetworkinfo`

- Դադարեցրեք Bitcoin Core դաեմոնը.:

`bitcoin-cli stop`
