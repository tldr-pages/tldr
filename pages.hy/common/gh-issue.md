# gh խնդիր

> Կառավարեք GitHub-ի խնդիրները:.
> Լրացուցիչ տեղեկություններ. <https://cli.github.com/manual/gh_issue>:.

- Ցուցադրել կոնկրետ խնդիր.:

`gh issue view {{issue_number}}`

- Ցուցադրել որոշակի խնդիր լռելյայն վեբ բրաուզերում.:

`gh issue view {{issue_number}} {{[-w|--web]}}`

- Ստեղծեք նոր խնդիր լռելյայն վեբ դիտարկիչում.:

`gh issue {{[new|create]}} {{[-w|--web]}}`

- Թվարկե՛ք `bug` պիտակի հետ կապված վերջին 10 խնդիրները.:

`gh issue {{[ls|list]}} {{[-L|--limit]}} 10 {{[-l|--label]}} "bug"`

- Թվարկեք որոշակի օգտագործողի կողմից արված փակ խնդիրները.:

`gh issue {{[ls|list]}} {{[-s|--state]}} closed {{[-A|--author]}} {{username}}`

- Ցուցադրել օգտվողին առնչվող խնդիրների կարգավիճակը հատուկ պահոցում.:

`gh issue status {{[-R|--repo]}} {{owner}}/{{repository}}`

- Վերաբացեք կոնկրետ խնդիր.:

`gh issue reopen {{issue_number}}`
