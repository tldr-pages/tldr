# jira sprint

> Beheer sprints in een Jira-projectbord.
> Meer informatie: <https://github.com/ankitpokhrel/jira-cli#sprint>.

- Toon sprints en hun issues in een verkennerweergave:

`jira sprint {{[ls|list]}}`

- Toon issues van de huidige sprint:

`jira sprint {{[ls|list]}} --current`

- Toon issues van de huidige sprint, toegewezen aan mij:

`jira sprint {{[ls|list]}} --current {{[-a|--assignee]}} $(jira me)`

- Toon issues met hoge prioriteit van de huidige sprint, toegewezen aan mij:

`jira sprint {{[ls|list]}} --current {{[-a|--assignee]}} $(jira me) {{[-y|--priority]}} High`

- Voeg issues toe aan een sprint met behulp van een interactieve prompt:

`jira sprint add`
