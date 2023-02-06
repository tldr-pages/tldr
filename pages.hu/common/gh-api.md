# gh api

> Hitelesített HTTP-kérelmeket intéz a GitHub API-hoz, és kinyomtatja a választ. További információ: <https://cli.github.com/manual/gh_api>.

- Az alparancs súgójának megjelenítése:

`gh api --help`

- Megjeleníti az aktuális adattár kiadásait JSON formátumban:

`gh api repos/:owner/:repo/releases`

- Reakció létrehozása egy adott kiadáshoz:

`gh api --header {{Accept:application/vnd.github.squirrel-girl-preview+json}} --raw-field '{{content=+1}}' {{repos/:owner/:repo/issues/123/reactions}}`

- Egy GraphQL lekérdezés eredményének megjelenítése JSON formátumban:

`gh api graphql --field {{name=':repo'}} --raw-field '{{query}}'`

- Kérés küldése egyéni HTTP-módszerrel:

`gh api --method {{POST}} {{endpoint}}`

- A HTTP-válasz fejlécek beillesztése a kimenetbe:

`gh api --include {{endpoint}}`

- Ne nyomtassa ki a válasz testét:

`gh api --silent {{endpoint}}`

- Kérés küldése egy adott GitHub Enterprise Serverre:

`gh api --hostname {{github.example.com}} {{endpoint}}`
