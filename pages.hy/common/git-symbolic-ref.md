# git խորհրդանշական-ռեֆ

> Կարդացեք, փոխեք կամ ջնջեք հղումներ պահող ֆայլերը:.
> Լրացուցիչ տեղեկություններ. <https://git-scm.com/docs/git-symbolic-ref>:.

- Պահպանեք հղումը անունով.:

`git symbolic-ref refs/{{name}} {{ref}}`

- Պահպանեք հղումը անունով, ներառյալ հաղորդագրությունը թարմացման պատճառաբանությամբ.:

`git symbolic-ref -m "{{message}}" refs/{{name}} refs/heads/{{branch_name}}`

- Կարդացեք հղումը անունով.:

`git symbolic-ref refs/{{name}}`

- Ջնջել հղումը անունով.:

`git symbolic-ref {{[-d|--delete]}} refs/{{name}}`

- Սկրիպտավորման համար թաքցրեք սխալները `--quiet`-ով և օգտագործեք `--short`՝ պարզեցնելու համար («refs/heads/X»-ը տպվում է որպես «X»):

`git symbolic-ref {{[-q|--quiet]}} --short refs/{{name}}`
