# gh ruleset

> Beheer GitHub repository-rulesets.
> Meer informatie: <https://cli.github.com/manual/gh_ruleset>.

- Toon alle rulesets voor de huidige repository:

`gh {{[rs|ruleset]}} {{[ls|list]}}`

- Toon alle rulesets voor een specifieke organisatie:

`gh {{[rs|ruleset]}} {{[ls|list]}} {{[-o|--org]}} {{organisatie_naam}}`

- Controleer de regels die van toepassing zijn op de huidige branch:

`gh {{[rs|ruleset]}} check`

- Controleer de regels die van toepassing zijn op een specifieke branch in een andere repository:

`gh {{[rs|ruleset]}} check {{branch_naam}} {{[-R|--repo]}} {{eigenaar}}/{{repository}}`

- Selecteer en bekijk interactief een ruleset voor de huidige repository:

`gh {{[rs|ruleset]}} view`

- Bekijk een specifieke ruleset via zijn ID:

`gh {{[rs|ruleset]}} view {{ruleset_id}}`

- Bekijk een ruleset op organisatieniveau via zijn ID:

`gh {{[rs|ruleset]}} view {{ruleset_id}} {{[-o|--org]}} {{organisatie_naam}}`

- Open de lijst met rulesets voor een specifieke repository in de browser:

`gh {{[rs|ruleset]}} {{[ls|list]}} {{[-R|--repo]}} {{eigenaar}}/{{repository}} {{[-w|--web]}}`
