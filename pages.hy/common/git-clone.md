# git clone

> Կլոնավորեք գոյություն ունեցող պահեստը:.
> Լրացուցիչ տեղեկություններ. <https://git-scm.com/docs/git-clone>:.

- Կլոնավորեք գոյություն ունեցող պահեստը նոր գրացուցակի մեջ (կանխադրված գրացուցակը պահեստի անունն է).:

`git clone {{remote_repository_location}} {{path/to/directory}}`

- Կլոնավորեք գոյություն ունեցող պահեստը և դրա ենթամոդուլները.:

`git clone --recursive {{remote_repository_location}}`

- Կլոնավորեք միայն գոյություն ունեցող պահեստի `.git` գրացուցակը.:

`git clone {{[-n|--no-checkout]}} {{remote_repository_location}}`

- Կլոնավորեք տեղական պահեստը.:

`git clone {{[-l|--local]}} {{path/to/local_repository}}`

- Հանգիստ կլոնավորեք.:

`git clone {{[-q|--quiet]}} {{remote_repository_location}}`

- Կլոնավորեք գոյություն ունեցող պահոցը՝ ստանալով լռելյայն ճյուղում միայն ամենավերջին 10 պարտավորությունները (օգտակար ժամանակ խնայելու համար).:

`git clone --depth 10 {{remote_repository_location}}`

- Կլոնավորեք գոյություն ունեցող պահոցը միայն որոշակի ճյուղ բերելով.:

`git clone {{[-b|--branch]}} {{name}} --single-branch {{remote_repository_location}}`

- Կլոնավորեք գոյություն ունեցող պահեստը՝ օգտագործելով հատուկ SSH հրաման.:

`git clone {{[-c|--config]}} core.sshCommand="{{ssh -i path/to/private_ssh_key}}" {{remote_repository_location}}`
