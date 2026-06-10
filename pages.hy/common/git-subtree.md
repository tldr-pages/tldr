# git ենթածառ

> Միավորել ենթածառերը կամ բաժանել պահեստը ենթածառերի:.
> Լրացուցիչ տեղեկություններ. <https://manned.org/git-subtree>:.

- Ավելացրեք Git պահեստը որպես ենթածառ և սեղմեք պարտավորությունները միասին.:

`git subtree add {{[-P|--prefix]}} {{path/to/directory}} --squash {{repository_url}} {{branch_name}}`

- Թարմացրեք ենթածառի պահոցն իր վերջին հանձնառությանը.:

`git subtree pull {{[-P|--prefix]}} {{path/to/directory}} {{repository_url}} {{branch_name}}`

- Միավորել վերջին փոփոխությունները մինչև վերջին ենթածառի պարտավորությունները ենթածառի մեջ.:

`git subtree merge {{[-P|--prefix]}} {{path/to/directory}} --squash {{repository_url}} {{branch_name}}`

- Push-ը պարտավորվում է ենթածառի պահեստ.:

`git subtree push {{[-P|--prefix]}} {{path/to/directory}} {{repository_url}} {{branch_name}}`

- Քաղեք նոր նախագծի պատմություն ենթածառի պատմությունից.:

`git subtree split {{[-P|--prefix]}} {{path/to/directory}} {{repository_url}} {{[-b|--branch]}} {{branch_name}}`
