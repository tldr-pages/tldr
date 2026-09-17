# az devops

> Gestisce le organizzazioni Azure DevOps.
> Parte di `azure-cli` (noto anche come `az`).
> Maggiori informazioni: <https://learn.microsoft.com/cli/azure/devops>.

- Imposta il Personal Access Token (PAT) per accedere a un'organizzazione specifica:

`az devops login {{[--org|--organization]}} {{url_organizzazione}}`

- Apri un progetto nel browser:

`az devops project show {{[-p|--project]}} {{nome_progetto}} --open`

- Elenca i membri di un team specifico che lavora su un progetto particolare:

`az devops team list-member {{[-p|--project]}} {{nome_progetto}} --team {{nome_team}}`

- Controlla la configurazione corrente della CLI Azure DevOps:

`az devops configure {{[-l|--list]}}`

- Configura il comportamento della CLI Azure DevOps impostando un progetto predefinito e un'organizzazione predefinita:

`az devops configure {{[-d|--defaults]}} project={{nome_progetto}} organization={{url_organizzazione}}`
