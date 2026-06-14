# bun pkg

> Կառավարեք `package.json` տվյալները `get`, `set`, `delete` և `fix` գործողություններով:.
> Լրացուցիչ տեղեկություններ. <https://bun.com/docs/pm/cli/pm#pkg>:.

- Ստացեք բոլոր հատկությունները `package.json`-ից:

`bun pm pkg get`

- Ստացեք մեկ սեփականություն.:

`bun pm pkg get {{property}}`

- Ստացեք բազմաթիվ հատկություններ.:

`bun pm pkg get {{property1 property2 property3 ...}}`

- Ստացեք ներկառուցված գույք.:

`bun pm pkg get {{property}}.{{attribute}}`

- Սահմանել սեփականություն.:

`bun pm pkg set {{property}}="{{value}}"`

- Ջնջել սեփականությունը.:

`bun pm pkg delete {{property}}`

- Ավտոմատ կերպով շտկել ընդհանուր խնդիրները `package.json`-ում.:

`bun pm pkg fix`
