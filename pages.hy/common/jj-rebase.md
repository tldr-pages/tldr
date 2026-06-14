# jj rebase

> Տեղափոխեք վերանայումները տարբեր ծնող(ներ):.
> Լրացուցիչ տեղեկություններ. <https://docs.jj-vcs.dev/latest/cli-reference/#jj-rebase>:.

- Տեղափոխեք տրված վերանայումները մեկ այլ ծնող(ներ).:

`jj rebase {{[-r|--revisions]}} {{revset}} {{[-d|--destination]}} {{revset}}`

- Տեղափոխեք տրված վերանայումները և նրանց բոլոր ժառանգները.:

`jj rebase {{[-s|--source]}} {{revset}} {{[-d|--destination]}} {{revset}}`

- Տեղափոխեք բոլոր վերանայումները տվյալ վերանայումներ պարունակող մասնաճյուղում.:

`jj rebase {{[-b|--branch]}} {{revset}} {{[-d|--destination]}} {{revset}}`

- Վերափոխումները տեղափոխեք այլ վերանայումներից առաջ և/կամ հետո.:

`jj rebase {{[-r|--revisions]}} {{revset}} {{[-B|--insert-before]}} {{revset}} {{[-A|--insert-after]}} {{revset}}`
