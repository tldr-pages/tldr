# func

> Azure Functions Core Tools: Develop and test Azure Functions locally.
> Local functions can connect to live Azure services, and can deploy a function app to an Azure subscription.
> More information: <https://learn.microsoft.com/azure/azure-functions/functions-run-local>.

- Create a new functions project:

`func init {{project}}`

- Create a new function:

`func new`

- Run functions locally:

`func start`

- Publish your code to a function app in Azure:

`func azure functionapp publish {{function}}`

- Download all settings from an existing function app:

`func azure functionapp fetch-app-settings {{function}}`

- Get the connection string for a specific storage account:

`func azure storage fetch-connection-string {{storage_account}}`
