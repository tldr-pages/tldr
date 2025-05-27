# az quantum

> Manage Azure Quantum workspaces and submit quantum jobs to providers (preview, requires quantum extension).
> More information: <https://learn.microsoft.com/en-us/cli/azure/quantum?view=azure-cli-latest>.

- Create a new Azure Quantum workspace:

`az quantum workspace create {{[-g|--resource-group]}} {{MyResourceGroup}} {{[-l|--location]}} {{MyLocation}} {{[-w|--workspace-name]}} {{MyWorkspace}} {{[-a|--storage-account]}} {{MyStorageAccountName}}`

- List all Azure Quantum workspaces:

`az quantum workspace list`

- Set a default Azure Quantum workspace:

`az quantum workspace set {{[-g|--resource-group]}} {{MyResourceGroup}} {{[-w|--workspace-name]}} {{MyWorkspace}}`

- Submit a QIR quantum job to a target:

`az quantum job submit {{[-g|--resource-group]}} {{MyResourceGroup}} {{[-w|--workspace-name]}} {{MyWorkspace}} {{[-l|--location]}} {{MyLocation}} {{[-t|--target-id]}} {{MyTarget}} --job-name {{MyJob}} --job-input-file {{MyQirBitcode.bc}} --job-input-format {{qir.v1}}`

- List all jobs in a Quantum Workspace:

`az quantum job list {{[-g|--resource-group]}} {{MyResourceGroup}} {{[-l|--location]}} {{MyLocation}} {{[-w|--workspace-name]}} {{MyWorkspace}}`

- Get the output of a quantum job:

`az quantum job output {{[-g|--resource-group]}} {{MyResourceGroup}} {{[-w|--workspace-name]}} {{MyWorkspace}} --job-id {{MyJob}}`

- List available provider offerings in a location:

`az quantum offerings list {{[-l|--location]}} {{MyLocation}}`

- Set a default target for job submissions:

`az quantum target set {{[-t|--target-id]}} {{MyTarget}}`
