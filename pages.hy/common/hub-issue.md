# հանգույցի խնդիր

> Կառավարեք Github-ի խնդիրները:.
> Լրացուցիչ տեղեկություններ. <https://hub.github.com/hub-issue.1.html>:.

- Թվարկե՛ք `bug` պիտակի հետ կապված վերջին 10 խնդիրները.:

`hub issue list {{[-L|--limit]}} {{10}} {{[-l|--labels]}} "{{bug}}"`

- Ցուցադրել կոնկրետ խնդիր.:

`hub issue show {{issue_number}}`

- Թվարկեք 10 փակ խնդիրներ, որոնք վերագրված են որոշակի օգտվողին.:

`hub issue {{[-s|--state]}} {{closed}} {{[-a|--assignee]}} {{username}} --limit {{10}}`
