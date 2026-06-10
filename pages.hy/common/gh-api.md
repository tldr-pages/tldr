# ղ ապի

> Կատարեք վավերացված HTTP հարցումներ GitHub API-ին և տպեք պատասխանը:.
> Լրացուցիչ տեղեկություններ. <https://cli.github.com/manual/gh_api>:.

- Ցուցադրել ընթացիկ պահեստի թողարկումները JSON ձևաչափով.:

`gh api repos/:owner/:repo/releases`

- Ստեղծեք արձագանք կոնկրետ հարցի համար.:

`gh api {{[-H|--header]}} {{Accept:application/vnd.github.squirrel-girl-preview+json}} {{[-f|--raw-field]}} '{{content=+1}}' {{repos/:owner/:repo/issues/123/reactions}}`

- Ցուցադրել GraphQL հարցման արդյունքը JSON ձևաչափով.:

`gh api graphql {{[-F|--field]}} {{name=':repo'}} {{[-f|--raw-field]}} '{{query}}'`

- Ուղարկեք հարցում՝ օգտագործելով հատուկ HTTP մեթոդ.:

`gh api {{[-X|--method]}} {{POST}} {{endpoint}}`

- Ներառեք HTTP պատասխանի վերնագրերը ելքի մեջ.:

`gh api {{[-i|--include]}} {{endpoint}}`

- Մի տպեք պատասխանի մարմինը.:

`gh api --silent {{endpoint}}`

- Հարցում ուղարկեք կոնկրետ GitHub Enterprise սերվերին.:

`gh api --hostname {{github.example.com}} {{endpoint}}`

- Ցուցադրել ենթահրամանի օգնությունը.:

`gh api --help`
