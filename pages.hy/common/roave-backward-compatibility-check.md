# roave-backward-compatibility-check

> Ստուգեք հետընթաց համատեղելիության ընդմիջումները PHP գրադարանի երկու տարբերակների միջև:.
> Լրացուցիչ տեղեկություններ. <https://github.com/Roave/BackwardCompatibilityCheck>:.

- Ստուգեք վերջին հատկորոշիչից ի վեր խախտված փոփոխությունները.:

`roave-backward-compatibility-check`

- Ստուգեք որոշակի պիտակի խախտման փոփոխությունները.:

`roave-backward-compatibility-check --from={{git_reference}}`

- Ստուգեք վերջին պիտակի և կոնկրետ հղումի միջև եղած փոփոխությունները.:

`roave-backward-compatibility-check --to={{git_reference}}`

- Ստուգեք Markdown-ի փոփոխություններն ու արդյունքները կոտրելու համար.:

`roave-backward-compatibility-check --format=markdown > {{results.md}}`
