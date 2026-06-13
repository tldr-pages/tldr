# jira me

> Toon de geconfigureerde `jira` gebruiker.
> Meer informatie: <https://github.com/ankitpokhrel/jira-cli#commands>.

- Toon de geconfigureerde `jira` gebruiker:

`jira me`

- Toon de issues die aan mij zijn toegewezen:

`jira issue {{[ls|list]}} {{[-a|--assignee]}} $(jira me)`

- Toon de issues uit de huidige sprint die aan mij zijn toegewezen:

`jira sprint {{[ls|list]}} --current {{[-a|--assignee]}} $(jira me)`

- Toon de help:

`jira me {{[-h|--help]}}`
