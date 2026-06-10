# gh նախագիծ

> Աշխատեք GitHub նախագծերի հետ:.
> Լրացուցիչ տեղեկություններ. <https://cli.github.com/manual/gh_project>:.

- Թվարկեք ներկայումս վավերացված օգտվողին պատկանող նախագծերը.:

`gh project {{[ls|list]}}`

- Թվարկեք նախագծերը, որոնք պատկանում են որոշակի օգտվողին կամ կազմակերպությանը.:

`gh project {{[ls|list]}} --owner {{owner}}`

- Դիտեք նախագիծը ըստ համարի.:

`gh project view {{number}} --owner {{owner}}`

- Ստեղծեք նոր նախագիծ.:

`gh project create --owner {{owner}} --title {{project_title}}`

- Ավելացրեք տարր (թողարկեք կամ քաշեք հարցում) նախագծին.:

`gh project item-add {{number}} --owner {{owner}} --url {{issue_or_pr_url}}`

- Թվարկեք տարրերը նախագծի մեջ.:

`gh project item-list {{number}} --owner {{owner}}`

- Փակել նախագիծը.:

`gh project close {{number}} --owner {{owner}}`
