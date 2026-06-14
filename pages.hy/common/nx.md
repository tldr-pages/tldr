# nx

> Կառավարեք `nx` աշխատանքային տարածքները:.
> Լրացուցիչ տեղեկություններ. <https://nx.dev/docs/reference/nx-commands>:.

- Կառուցեք կոնկրետ նախագիծ.:

`nx build {{project}}`

- Փորձարկել կոնկրետ նախագիծ.:

`nx test {{project}}`

- Իրականացնել թիրախ կոնկրետ նախագծի վրա.:

`nx run {{project}}:{{target}}`

- Կատարել թիրախ մի քանի նախագծերի վրա.:

`nx run-many --target {{target}} --projects {{project1}},{{project2}}`

- Աշխատանքային տարածքի բոլոր նախագծերի վրա նպատակ դրեք.:

`nx run-many --target {{target}} --all`

- Իրականացնել թիրախ միայն այն նախագծերի վրա, որոնք փոխվել են.:

`nx affected --target {{target}}`
