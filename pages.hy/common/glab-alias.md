# glab alias

> Կառավարեք GitLab CLI հրամանի կեղծանունները:.
> Լրացուցիչ տեղեկություններ. <https://gitlab.com/gitlab-org/cli/-/blob/main/docs/source/alias/_index.md>:.

- Թվարկեք բոլոր կեղծանունները՝ `glab`-ը կազմաձևված է օգտագործելու համար՝:

`glab alias list`

- Ստեղծեք `glab` ենթահրամանի կեղծանունը՝:

`glab alias set {{mrv}} '{{mr view}}'`

- Սահմանեք shell հրամանը որպես `glab` ենթահրաման:

`glab alias set {{[-s|--shell]}} {{alias_name}} {{command}}`

- Ջնջել հրամանի դյուրանցումը.:

`glab alias delete {{alias_name}}`

- Ցուցադրել ենթահրամանի օգնությունը.:

`glab alias`
