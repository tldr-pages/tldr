# az devops

> Gestisce le organizzazioni su Azure DevOps.
> Parte della `azure-cli`
> Più informazioni: <https://learn.microsoft.com/en-us/cli/azure/devops?view=azure-cli-latest>

- Imposta il Personal Access Token (PAT) per accedere a una specifica organizzazione

`az devops login --organization {{organization_URL}}`

- Apre uno specifico progetto su browser

`az devops project show --project {{project_name}} --open`

- Elenca i membri di uno specifico team al lavoro su uno specifico progetto 
- 
`az devops team list-member --project {{project_name}} --team {{team_name}}`

- Visualizza la configurazione corrente della Azure DevOps CLI

`az devops configure --list`

- Configura il comportamento della Azure DevOps CLI impostando un progetto predefinito e un'organizzazione predefinita

`az devops configure --defaults project={{project_name}} organization={{organization_URL}}`