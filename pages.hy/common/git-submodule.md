# git ենթամոդուլ

> Ստուգեք, թարմացրեք և կառավարեք ենթամոդուլները:.
> Լրացուցիչ տեղեկություններ. <https://git-scm.com/docs/git-submodule>:.

- Դիտեք առկա ենթամոդուլները և յուրաքանչյուրի համար դուրս գրված պարտավորությունները.:

`git submodule`

- Տեղադրեք պահեստի ենթամոդուլները (թվարկված են `.gitmodules`-ում).:

`git submodule update --init --recursive`

- Ավելացրեք Git պահոց՝ որպես ընթացիկի ենթամոդուլ.:

`git submodule add {{repository_url}}`

- Ավելացրեք Git պահոցը որպես ընթացիկի ենթամոդուլ, որոշակի գրացուցակում.:

`git submodule add {{repository_url}} {{path/to/directory}}`

- Թարմացրեք ենթամոդուլները իրենց վերջին պարտավորություններին.:

`git submodule update --remote`

- Փոխել ենթամոդուլի URL-ը.:

`git submodule set-url {{path/to/submodule}} {{new_url}}`

- Ապագրանցել ենթամոդուլը (օրինակ՝ նախքան այն հանել պահեստից `git rm`-ով):

`git submodule deinit {{path/to/submodule}}`
