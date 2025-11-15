# gh pr

> Beheer GitHub pull requests.
> Sommige subcommando's zoals `create` hebben hun eigen gebruiksdocumentatie.
> Meer informatie: <https://cli.github.com/manual/gh_pr>.

- Maak een pull request aan:

`gh pr {{[new|create]}}`

- Bekijk een specifieke pull request lokaal:

`gh {{[co|pr checkout]}} {{pr_nummer|url|branch}}`

- Bekijk de gemaakte wijzigingen in de pull request voor de huidige branch:

`gh pr diff`

- Keur de pull request voor de huidige branch goed:

`gh pr review {{[-a|--approve]}}`

- Voeg de pull request voor de huidige branch interactief samen:

`gh pr merge`

- Bewerk een pull request interactief:

`gh pr edit`

- Bewerk de basisbranch van een pull request:

`gh pr edit {{[-B|--base]}} {{branch_naam}}`

- Toon de status van de pull requests van de huidige repository:

`gh pr status`
