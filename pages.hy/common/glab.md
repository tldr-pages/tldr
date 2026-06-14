#գլաբ

> Անխափան աշխատեք GitLab-ի հետ:.
> Որոշ ենթահրամաններ, ինչպիսիք են `config`-ն, ունեն իրենց օգտագործման փաստաթղթերը:.
> Լրացուցիչ տեղեկություններ. <https://gitlab.com/gitlab-org/cli/-/tree/main/docs/source>:.

- Կլոնավորեք GitLab-ի պահոցը տեղում.:

`glab repo clone {{owner}}/{{repository}}`

- Ստեղծեք նոր թողարկում.:

`glab issue create`

- Դիտեք և զտեք ընթացիկ պահոցի բաց թողարկումները.:

`glab issue list`

- Դիտեք խնդիրը լռելյայն դիտարկիչում.:

`glab issue view {{[-w|--web]}} {{issue_number}}`

- Ստեղծեք միաձուլման հարցում.:

`glab mr create`

- Դիտեք քաշման հարցումը լռելյայն վեբ բրաուզերում.:

`glab mr view {{[-w|--web]}} {{pr_number}}`

- Ստուգեք տեղական ձգողականության հատուկ հարցում.:

`glab {{[co|mr checkout]}} {{pr_number}}`
