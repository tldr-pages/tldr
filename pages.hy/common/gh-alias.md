# gh alias

> Կառավարեք GitHub CLI հրամանի կեղծանունները:.
> Լրացուցիչ տեղեկություններ. <https://cli.github.com/manual/gh_alias>:.

- Թվարկեք բոլոր կեղծանունները՝ `gh`-ը կազմաձևված է օգտագործելու համար՝:

`gh alias {{[ls|list]}}`

- Ստեղծեք `gh` ենթահրամանի կեղծանունը՝:

`gh alias set {{pv}} '{{pr view}}'`

- Սահմանեք shell հրամանը որպես `gh` ենթահրաման:

`gh alias set {{[-s|--shell]}} {{alias_name}} {{command}}`

- Ջնջել հրամանի դյուրանցումը.:

`gh alias delete {{alias_name}}`

- Ցուցադրել ենթահրամանի օգնությունը.:

`gh alias`
