# tlmgr conf

> Կառավարեք TeX Live կոնֆիգուրացիան:.
> Լրացուցիչ տեղեկություններ. <https://www.tug.org/texlive/doc/tlmgr.html#conf>:.

- Ցույց տալ ընթացիկ TeX Live կոնֆիգուրացիան.:

`tlmgr conf`

- Ցույց տալ ընթացիկ `texmf`, `tlmgr` կամ `updmap` կոնֆիգուրացիան՝:

`tlmgr conf {{texmf|tlmgr|updmap}}`

- Ցույց տալ միայն կոնկրետ կազմաձևման տարբերակ.:

`tlmgr conf {{texmf|tlmgr|updmap}} {{configuration_key}}`

- Սահմանեք հատուկ կազմաձևման տարբերակ.:

`tlmgr conf {{texmf|tlmgr|updmap}} {{configuration_key}} {{value}}`

- Ջնջել որոշակի կազմաձևման տարբերակ.:

`tlmgr conf {{texmf|tlmgr|updmap}} --delete {{configuration_key}}`

- Անջատել համակարգային զանգերի կատարումը `\write18`-ի միջոցով.:

`tlmgr conf texmf {{shell_escape}} {{0}}`

- Ցույց տալ բոլոր լրացուցիչ `texmf` ծառերը՝:

`tlmgr conf auxtrees show`
