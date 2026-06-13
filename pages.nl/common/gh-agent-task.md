# gh agent-task

> Beheer GitHub-agenttaken.
> Meer informatie: <https://cli.github.com/manual/gh_agent-task>.

- Toon de nieuwste agenttaken:

`gh {{[agent|agent-task]}} list`

- Maak een nieuwe agenttaak aan voor de huidige repository:

`gh {{[agent|agent-task]}} create "{{Verbeter de prestatie van de dataverwerkingspijplijn}}"`

- Maak een nieuwe agenttaak aan vanuit een bestand:

`gh {{[agent|agent-task]}} create {{[-F|--from-file]}} {{pad/naar/bestand}}`

- Toon details over een specifieke agenttaak:

`gh {{[agent|agent-task]}} view {{sessie_id|pr_nummer|url|branch}}`

- Toon de log van een specifieke agenttaak:

`gh {{[agent|agent-task]}} view --log {{sessie_id|pr_nummer|url|branch}}`
