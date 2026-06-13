# jira issue

> Beheer issues in een Jira-project.
> Meer informatie: <https://github.com/ankitpokhrel/jira-cli#issue>.

- Toon recente issues:

`jira issue {{[ls|list]}}`

- Toon issues toegewezen aan een specifieke gebruiker:

`jira issue {{[ls|list]}} {{[-a|--assignee]}} "{{email_of_gebruikersnaam}}"`

- Toon issues met hoge prioriteit die zijn toegewezen aan mij:

`jira issue {{[ls|list]}} {{[-a|--assignee]}} $(jira me) {{[-y|--priority]}} High`

- Maak een issue aan met behulp van een interactieve prompt:

`jira issue create`

- Bewerk een issue met behulp van een interactieve prompt:

`jira issue edit`

- Wijs een gebruiker toe aan een issue met behulp van een interactieve prompt:

`jira issue {{[asg|assign]}}`

- Verplaats een issue naar een bepaalde status:

`jira issue {{[mv|move]}} {{issue_id}} "{{In Progress}}"`

- Open een issue in de terminal met `less`:

`jira issue view {{issue_id}}`
