# terraform workspace

> Manage Terraform workspaces for multiple environments.
> More information: <https://developer.hashicorp.com/terraform/cli/commands/workspace>.

- List all workspaces:

`terraform workspace list`

- Show the name of the current workspace:

`terraform workspace show`

- Create a new workspace:

`terraform workspace new {{workspace_name}}`

- Select an existing workspace:

`terraform workspace select {{workspace_name}}`

- Select a workspace, creating it if it doesn't exist:

`terraform workspace select -or-create {{workspace_name}}`

- Delete a workspace:

`terraform workspace delete {{workspace_name}}`

- Delete a workspace, even if it is tracking resources:

`terraform workspace delete -force {{workspace_name}}`
