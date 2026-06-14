# jj ինտերդիֆ

> Համեմատեք երկու վերանայումների փոփոխությունները:.
> Լրացուցիչ տեղեկություններ. <https://docs.jj-vcs.dev/latest/cli-reference/#jj-interdiff>:.

- Համեմատեք փոփոխությունները վերանայումից մինչև աշխատանքային օրինակ.:

`jj interdiff {{[-f|--from]}} {{revset}}`

- Համեմատեք փոփոխությունները վերանայումից մեկ այլ վերանայման.:

`jj interdiff {{[-f|--from]}} {{from_revset}} {{[-t|--to]}} {{to_revset}}`

- Համեմատեք փոփոխությունները միայն կոնկրետ ուղիներում.:

`jj interdiff {{[-f|--from]}} {{from_revset}} {{[-t|--to]}} {{to_revset}} {{filesets}}`

- Ցույց տալ փոփոխությունների ամփոփագիրը.:

`jj interdiff {{[-f|--from]}} {{revset}} {{[-s|--summary]}}`

- Ցույց տալ տարբեր վիճակագրությունը.:

`jj interdiff {{[-f|--from]}} {{revset}} --stat`

- Ցույց տալ Git-ֆորմատի տարբերությունը.:

`jj interdiff {{[-f|--from]}} {{revset}} --git`

- Ցույց տալ բառի մակարդակի տարբերությունը միայն գույնով նշված փոփոխություններով.:

`jj interdiff {{[-f|--from]}} {{revset}} --color-words`
