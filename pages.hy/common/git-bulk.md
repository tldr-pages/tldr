#git զանգվածային

> Կատարել գործողություններ բազմաթիվ Git պահեստներում:.
> `git-extras`-ի մի մասը:.
> Լրացուցիչ տեղեկություններ. <https://github.com/tj/git-extras/blob/main/Commands.md#git-bulk>:.

- Գրանցեք ընթացիկ գրացուցակը որպես աշխատանքային տարածք.:

`git bulk --addcurrent {{workspace_name}}`

- Գրանցեք աշխատանքային տարածք զանգվածային գործառնությունների համար.:

`git bulk --addworkspace {{workspace_name}} /{{path/to/repository}}`

- Կլոնավորեք պահեստը որոշակի գրացուցակի ներսում, այնուհետև գրանցեք պահեստը որպես աշխատանքային տարածք.:

`git bulk --addworkspace {{workspace_name}} /{{path/to/parent_directory}} --from {{remote_repository_location}}`

- Կլոնավորեք պահեստները նոր տողով առանձնացված հեռավոր վայրերի ցանկից, այնուհետև գրանցեք դրանք որպես աշխատանքային տարածքներ.:

`git bulk --addworkspace {{workspace_name}} /{{path/to/root_directory}} --from /{{path/to/file}}`

- Նշեք բոլոր գրանցված աշխատանքային տարածքները.:

`git bulk --listall`

- Գործարկեք Git հրամանը ընթացիկ աշխատանքային տարածքի պահեստներում.:

`git bulk {{command}} {{command_arguments}}`

- Հեռացրեք որոշակի աշխատանքային տարածք.:

`git bulk --removeworkspace {{workspace_name}}`

- Հեռացրեք բոլոր աշխատանքային տարածքները.:

`git bulk --purge`
