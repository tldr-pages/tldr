# hledger register

> Ցույց տալ գործարքները և ընթացիկ մնացորդները մեկ հաշվում, յուրաքանչյուր գործարք մեկ տողում:.
> Լրացուցիչ տեղեկություններ. <https://hledger.org/hledger.html#aregister>:.

- Ցույց տալ գործարքները և ընթացիկ մնացորդը `assets:bank:checking` հաշվում՝:

`hledger {{[areg|aregister]}} assets:bank:checking`

- Ցույց տալ գործարքները և ընթացիկ մնացորդը առաջին հաշվում, որի անունը պարունակում է `savings`:

`hledger {{[areg|aregister]}} savings`

- Ցույց տալ չեկային հաշվի մաքրված գործարքները՝ նշված լայնությամբ.:

`hledger {{[areg|aregister]}} checking {{[-C|--cleared]}} {{[-w|--width]}} {{120}}`

- Ցույց տալ ստուգման գրանցամատյանը, ներառյալ կանխատեսման կանոններից կատարված գործարքները.:

`hledger {{[areg|aregister]}} checking --forecast`
