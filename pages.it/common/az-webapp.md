# az webapp

> Gestisce le applicazioni web ospitate nei servizi cloud Azure.
> Parte di `azure-cli` (noto anche come `az`).
> Maggiori informazioni: <https://learn.microsoft.com/cli/azure/webapp>.

- Elenca i runtime disponibili per un'applicazione web:

`az webapp list-runtimes {{[-os|--os-type]}} {{windows|linux}}`

- Crea un'applicazione web:

`az webapp up {{[-n|--name]}} {{nome}} {{[-l|--location]}} {{posizione}} {{[-r|--runtime]}} {{runtime}}`

- Elenca tutte le applicazioni web:

`az webapp list`

- Elimina un'applicazione web specifica:

`az webapp delete {{[-n|--name]}} {{nome}} {{[-g|--resource-group]}} {{gruppo_risorse}}`
