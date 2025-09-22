# gh

> Werk gemakkelijk met GitHub.
> Sommige subcommando's zoals `config` hebben hun eigen gebruiksdocumentatie.
> Meer informatie: <https://cli.github.com/manual/gh>.

- Kloon een GitHub-repository lokaal:

`gh repo clone {{eigenaar}}/{{repository}}`

- Maak een nieuw issue aan:

`gh issue {{[new|create]}}`

- Bekijk en filter de openstaande issues van de huidige repository:

`gh issue {{[ls|list]}}`

- Bekijk een issue in de standaard webbrowser:

`gh issue view {{[-w|--web]}} {{issue_nummer|url}}`

- Maak een pull request aan:

`gh pr {{[new|create]}}`

- Bekijk een pull request in de standaard webbrowser:

`gh pr view {{[-w|--web]}} {{pr_nummer|url|branch}}`

- Bekijk een pull request lokaal:

`gh {{[co|pr checkout]}} {{pr_number|url|branch}}`

- Controleer de status van pull requests van een repository:

`gh pr status`
