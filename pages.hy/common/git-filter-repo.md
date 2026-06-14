# git filter-repo

> Git պատմությունը վերաշարադրելու բազմակողմանի գործիք:.
> Տես նաև՝ `bfg`:.
> Լրացուցիչ տեղեկություններ. <https://github.com/newren/git-filter-repo>:.

- Փոխարինեք զգայուն տողը բոլոր ֆայլերում.:

`git filter-repo --replace-text <(echo '{{find}}==>{{replacement}}')`

- Արտահանեք մեկ թղթապանակ՝ պահպանելով պատմությունը.:

`git filter-repo --path {{path/to/folder}}`

- Հեռացրեք մեկ թղթապանակ՝ պահպանելով պատմությունը.:

`git filter-repo --path {{path/to/folder}} --invert-paths`

- Տեղափոխեք ամեն ինչ ենթաթղթապանակից մեկ մակարդակ վերև.:

`git filter-repo --path-rename {{path/to/folder}}/:`
