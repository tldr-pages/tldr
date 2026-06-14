# jj վերադարձ

> Կիրառել տվյալ վերանայում(ներ)ի հակառակ կողմը:.
> Լրացուցիչ տեղեկություններ. <https://docs.jj-vcs.dev/latest/cli-reference/#jj-revert>:.

- Կիրառեք վերափոխումների հակառակը, որոնք նշված են նշված վերահաշվարկներով (օրինակ՝ `B::D`, `A..D`, `B|C|D` և այլն):

`jj revert {{[-r|--revisions]}} {{revsets}}`

- Կիրառեք հակառակը նշված վերանայումների վերևում.:

`jj revert {{[-r|--revisions]}} {{revsets}} {{[-d|--destination]}} {{revsets}}`

- Կիրառեք հակառակը նշված վերանայումներից առաջ և/կամ հետո.:

`jj revert {{[-r|--revisions]}} {{revsets}} {{[-B|--insert-before]}} {{revsets}} {{[-A|--insert-after]}} {{revsets}}`
