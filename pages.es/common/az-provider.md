# az provider

> Administra proveedores de recursos.
> Parte de `azure-cli` (también conocido como `az`).
> Más información: <https://learn.microsoft.com/cli/azure/provider>.

- Registra un proveedor:

`az provider register {{[-n|--namespace]}} {{Microsoft.PolicyInsights}}`

- Cancela el registro de un proveedor:

`az provider unregister {{[-n|--namespace]}} {{Microsoft.Automation}}`

- Lista todos los proveedores de una suscripción:

`az provider list`

- Muestra información sobre un proveedor específico:

`az provider show {{[-n|--namespace]}} {{Microsoft.Storage}}`

- Lista todos los tipos de recursos para un proveedor específico:

`az provider list --query "[?namespace=='{{Microsoft.Network}}'].resourceTypes[].resourceType"`
