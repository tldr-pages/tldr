# func

> Funcții Azure Instrumente de bază: Dezvoltarea și testarea funcțiilor Azure la nivel local.
> Funcțiile locale se pot conecta la serviciile Azure live și pot implementa o aplicație funcție la un abonament Azure.
> Mai multe informaţii: <https://docs.microsoft.com/azure/azure-functions/functions-run-local>

- Creați un proiect nou de funcții:

`func init {{project}}`

- Creați o nouă funcție:

`func new`

- Rulați funcții la nivel local:

`func start`

- Publicați codul într-o aplicație funcție în Azure:

`func azure functionapp publish {{function}}`

- Descărcați toate setările dintr-o aplicație funcțională existentă:

`func azure functionapp fetch-app-settings {{function}}`

- Obțineți șirul de conexiune pentru un anumit cont de stocare:

`func azure storage fetch-connection-string {{storage_account}}`
