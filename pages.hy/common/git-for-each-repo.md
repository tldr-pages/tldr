# git յուրաքանչյուր ռեպո-ի համար

> Գործարկեք Git հրամանը պահեստների ցանկում:.
> Նշում. Այս հրամանը փորձնական է և կարող է փոխվել:.
> Լրացուցիչ տեղեկություններ. <https://git-scm.com/docs/git-for-each-repo>:.

- Գործարկեք սպասարկումը `maintenance.repo` օգտվողի կազմաձևման փոփոխականում պահվող պահեստների ցանկից յուրաքանչյուրում.:

`git for-each-repo --config maintenance.repo {{maintenance run}}`

- Գործարկեք `git pull` յուրաքանչյուր պահեստում, որը նշված է գլոբալ կազմաձևման փոփոխականում.:

`git for-each-repo --config {{global_configuration_variable}} {{pull}}`
