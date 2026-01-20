# jira

> Interfaccia (terze parti) per interagire con Jira.
> Nota: È necessario ottenere un token API Jira ed esportarlo nella shell come variabile `$JIRA_API_TOKEN`.
> Maggiori informazioni: <https://github.com/ankitpokhrel/jira-cli#commands>.

- Crea un file di configurazione (richiesto prima di usare `jira`):

`jira init`

- Elenca le issues recenti:

`jira issue {{[ls|list]}}`

- Elenca issues non assegnate con alta priorità:

`jira issue {{[ls|list]}} {{[-a|--assignee]}} x {{[-y|--priority]}} High`

- Elenca issues dallo sprint corrente, assegnate a me:

`jira sprint {{[ls|list]}} --current {{[-a|--assignee]}} $(jira me)`

- Crea una nuova issue con issue genitore:

`jira issue create {{[-P|--parent]}} {{parent}}`

- Apri un'issue nel browser:

`jira open {{123}}`
