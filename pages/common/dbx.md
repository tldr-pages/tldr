# dbx

> Interact with the Databricks platform.
> Note: This tool has been retired and it is recommended to use Databricks Asset Bundles instead.
> More information: <https://dbx.readthedocs.io/en/latest/reference/cli/#dbx>.

- Create a new `dbx` project in the current working directory:

`dbx configure --profile {{DEFAULT}}`

- Sync local files from the specified path to DBFS and watch for changes:

`dbx sync dbfs --source {{path/to/directory}} --dest {{path/to/remote_directory}}`

- Deploy the specified workflow to artifact storage:

`dbx deploy {{workflow_name}}`

- Launch the specified workflow after deploying it:

`dbx launch {{workflow_name}}`
