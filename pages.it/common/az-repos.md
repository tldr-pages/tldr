# az repos

> Gestisce i repository Azure DevOps.
> Parte di `azure-cli` (noto anche come `az`).
> Maggiori informazioni: <https://learn.microsoft.com/cli/azure/repos>.

- Elenca tutti i repository in un progetto specifico:

`az repos list {{[-p|--project]}} {{nome_progetto}}`

- Aggiunge una policy su un branch specifico di un repository specifico per restringere la merge base:

`az repos policy merge-strategy create --repository-id {{id_repository_da_elenco_repos}} --branch {{nome_branch}} --blocking --enabled --allow-no-fast-forward false --allow-rebase true --allow-rebase-merge true --allow-squash true`

- Aggiunge una validazione build su un repository specifico, usando una pipeline build esistente, da attivare automaticamente su aggiornamento sorgente:

`az repos policy build create --repository-id {{id_repository}} --build-definition-id {{id_pipeline_build}} --branch main --blocking --enabled --queue-on-source-update-only true --display-name {{nome}} --valid-duration {{minuti}}`

- Elenca tutte le Pull Request attive su un repository specifico all'interno di un progetto specifico:

`az repos pr list {{[-p|--project]}} {{nome_progetto}} {{[-r|--repository]}} {{nome_repository}} --status active`
