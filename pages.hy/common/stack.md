# բուրգ

> Կառավարեք Haskell նախագծերը:.
> Լրացուցիչ տեղեկություններ. <https://docs.haskellstack.org/en/stable/commands/>:.

- Ստեղծեք նոր փաթեթ.:

`stack new {{package}} {{template}}`

- Կազմել փաթեթ.:

`stack build`

- Փորձարկումներ կատարեք փաթեթի ներսում.:

`stack test`

- Կազմեք նախագիծ և նորից կազմեք ամեն անգամ, երբ ֆայլը փոխվում է.:

`stack build --file-watch`

- Կազմեք նախագիծ և կատարեք հրաման կոմպիլյացիայից հետո.:

`stack build --exec "{{command}}"`

- Գործարկեք ծրագիր և փոխանցեք դրա փաստարկը.:

`stack exec {{program}} -- {{argument}}`
