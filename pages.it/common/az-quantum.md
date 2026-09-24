# az quantum

> Gestisce i workspace Azure Quantum e invia job quantistici ai provider (preview, richiede estensione quantum).
> Maggiori informazioni: <https://learn.microsoft.com/cli/azure/quantum>.

- Crea un nuovo workspace Azure Quantum:

`az quantum workspace create {{[-g|--resource-group]}} {{GruppoRisorse}} {{[-l|--location]}} {{Posizione}} {{[-w|--workspace-name]}} {{Workspace}} {{[-a|--storage-account]}} {{NomeAccountArchiviazione}}`

- Elenca tutti i workspace Azure Quantum:

`az quantum workspace list`

- Imposta un workspace Azure Quantum predefinito:

`az quantum workspace set {{[-g|--resource-group]}} {{GruppoRisorse}} {{[-w|--workspace-name]}} {{Workspace}}`

- Invia un job quantistico QIR a un target:

`az quantum job submit {{[-g|--resource-group]}} {{GruppoRisorse}} {{[-w|--workspace-name]}} {{Workspace}} {{[-l|--location]}} {{Posizione}} {{[-t|--target-id]}} {{Id}} --job-name {{Job}} --job-input-file {{QirBitcode.bc}} --job-input-format {{qir.v1}}`

- Elenca tutti i job in un Quantum Workspace:

`az quantum job list {{[-g|--resource-group]}} {{GruppoRisorse}} {{[-l|--location]}} {{Posizione}} {{[-w|--workspace-name]}} {{Workspace}}`

- Ottiene l'output di un job quantistico:

`az quantum job output {{[-g|--resource-group]}} {{GruppoRisorse}} {{[-w|--workspace-name]}} {{Workspace}} --job-id {{Job}}`

- Elenca le offerte dei provider disponibili in una posizione:

`az quantum offerings list {{[-l|--location]}} {{Posizione}}`

- Imposta un target predefinito per l'invio dei job:

`az quantum target set {{[-t|--target-id]}} {{Id}}`
