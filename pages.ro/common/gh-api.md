# gh api

> Face cereri HTTP autentificate la API-ul GitHub și imprimă răspunsul.
> Mai multe informaţii: <https://cli.github.com/manual/gh_api>

- Afișează ajutorul subcomenzii:

`gh api --help`

- Afișează versiunile pentru depozitul curent în format JSON:

`gh api repos/:owner/:repo/releases`

- Creați o reacție pentru o anumită problemă:

`gh api --header {{Accept:application/vnd.github.squirrel-girl-preview+json}} --raw-field '{{content=+1}}' {{repos/:owner/:repo/issues/123/reactions}}`

- Afișează rezultatul unei interogări GraphQL în format JSON:

`gh api graphql --field {{name=':repo'}} --raw-field '{{query}}'`

- Trimiteți o solicitare utilizând o metodă HTTP personalizată:

`gh api --method {{POST}} {{endpoint}}`

- Includeți anteturile de răspuns HTTP în ieșire:

`gh api --include {{endpoint}}`

- Nu imprimaţi corpul de răspuns:

`gh api --silent {{endpoint}}`

- Trimiteți o cerere către un anumit server GitHub Enterprise:

`gh api --hostname {{github.example.com}} {{endpoint}}`
