# գլաբի խնդիր

> Կառավարեք GitLab-ի խնդիրները:.
> Լրացուցիչ տեղեկություններ. <https://gitlab.com/gitlab-org/cli/-/blob/main/docs/source/issue/_index.md>:.

- Ցուցադրել կոնկրետ խնդիր.:

`glab issue view {{issue_number}}`

- Ցուցադրել որոշակի խնդիր լռելյայն վեբ բրաուզերում.:

`glab issue view {{issue_number}} {{[-w|--web]}}`

- Ստեղծեք նոր խնդիր լռելյայն վեբ դիտարկիչում.:

`glab issue create --web`

- Թվարկե՛ք `bug` պիտակի հետ կապված վերջին 10 խնդիրները.:

`glab issue list {{[-P|--per-page]}} {{10}} {{[-l|--label]}} "{{bug}}"`

- Թվարկեք որոշակի օգտագործողի կողմից արված փակ խնդիրները.:

`glab issue list {{[-c|--closed]}} --author {{username}}`

- Վերաբացեք կոնկրետ խնդիր.:

`glab issue reopen {{issue_number}}`
