# az quantum

> Manage Azure Quantum workspaces and submit quantum jobs to providers (preview, requires quantum extension).
> More information: <https://learn.microsoft.com/cli/azure/quantum>.

- Create a new Azure Quantum workspace:

`az quantum workspace create {{[-g|--resource-group]}} {{ResourceGroup}} {{[-l|--location]}} {{Location}} {{[-w|--workspace-name]}} {{Workspace}} {{[-a|--storage-account]}} {{MyStorageAccountName}}`

- List all Azure Quantum workspaces:

`az quantum workspace list`

- Set a default Azure Quantum workspace:

`az quantum workspace set {{[-g|--resource-group]}} {{ResourceGroup}} {{[-w|--workspace-name]}} {{Workspace}}`

- Submit a QIR quantum job to a target:

`az quantum job submit {{[-g|--resource-group]}} {{ResourceGroup}} {{[-w|--workspace-name]}} {{Workspace}} {{[-l|--location]}} {{Location}} {{[-t|--target-id]}} {{Id}} --job-name {{Job}} --job-input-file {{QirBitcode.bc}} --job-input-format {{qir.v1}}`

- List all jobs in a Quantum Workspace:

`az quantum job list {{[-g|--resource-group]}} {{ResourceGroup}} {{[-l|--location]}} {{Location}} {{[-w|--workspace-name]}} {{Workspace}}`

- Get the output of a quantum job:

`az quantum job output {{[-g|--resource-group]}} {{ResourceGroup}} {{[-w|--workspace-name]}} {{Workspace}} --job-id {{Job}}`

- List available provider offerings in a location:

`az quantum offerings list {{[-l|--location]}} {{Location}}`

- Set a default target for job submissions:

`az quantum target set {{[-t|--target-id]}} {{Id}}`
