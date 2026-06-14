# gh ընդլայնում

> Կառավարեք ընդլայնումները GitHub CLI-ի համար:.
> Լրացուցիչ տեղեկություններ. <https://cli.github.com/manual/gh_extension>:.

- Նախաձեռնեք նոր GitHub CLI ընդլայնման նախագիծը նույն անունով գրացուցակում.:

`gh {{[ext|extension]}} create {{extension_name}}`

- Տեղադրեք ընդլայնում GitHub պահոցից.:

`gh {{[ext|extension]}} install {{owner}}/{{repository}}`

- Տեղադրված ընդլայնումների ցանկ.:

`gh {{[ext|extension]}} {{[ls|list]}}`

- Թարմացրեք հատուկ ընդլայնում.:

`gh {{[ext|extension]}} upgrade {{extension_name}}`

- Թարմացրեք բոլոր ընդարձակումները.:

`gh {{[ext|extension]}} upgrade --all`

- Տեղադրված ընդլայնումների ցանկ.:

`gh {{[ext|extension]}} {{[ls|list]}}`

- Հեռացնել ընդլայնումը.:

`gh {{[ext|extension]}} remove {{extension_name}}`

- Ցուցադրել օգնություն ենթահրամանի մասին.:

`gh {{[ext|extension]}} {{subcommand}} {{[-h|--help]}}`
