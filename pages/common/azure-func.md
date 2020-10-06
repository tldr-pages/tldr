# func

> Azure Functions Core Tools lets you develop and test your functions on your local computer from the command prompt or terminal.
> Your local functions can connect to live Azure services, and you can deploy a function app to your Azure subscription.
> More information: <https://docs.microsoft.com/en-us/azure/azure-functions/functions-run-local>

- Create a new functions project:

`func init {{project}}`

- Create a new function:

`func new`

- Run functions locally:

`func start`

- Publish your local code to a function app in Azure:

`func azure functionapp publish {{function}}`

- Download all settings from an existing function app:

`func azure functionapp fetch-app-settings {{function}}`

- Get the Connection string for a specific storage account:

`func azure storage fetch-connection-string {{storageAccount}}`
