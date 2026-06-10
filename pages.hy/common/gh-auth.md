# gh auth

> Նույնականացում GitHub հոսթի միջոցով:.
> Լրացուցիչ տեղեկություններ. <https://cli.github.com/manual/gh_auth>:.

- Մուտք գործեք ինտերակտիվ հուշումով.:

`gh auth login`

- Մուտք գործեք թոքենով՝ `stdin`-ից (ստեղծվել է <https://github.com/settings/tokens>-ում):

`echo {{your_token}} | gh auth login --with-token`

- Ստուգեք, արդյոք մուտք եք գործել.:

`gh auth status`

- Դուրս գալ.:

`gh auth logout`

- Մուտք գործեք հատուկ GitHub Enterprise սերվերով.:

`gh auth login {{[-h|--hostname]}} {{github.example.com}}`

- Թարմացրեք նիստը՝ համոզվելու համար, որ նույնականացման հավատարմագրերն ունեն ճիշտ նվազագույն շրջանակներ (հեռացնում է նախկինում պահանջված լրացուցիչ շրջանակները).:

`gh auth refresh`

- Ընդլայնել թույլտվությունների շրջանակները.:

`gh auth refresh {{[-s|--scopes]}} {{repo,admin:repo_hook,admin:org,admin:public_key,admin:org_hook,...}}`
