# az devops

> Manage Azure DevOps organizations.
> Part of `azure-cli` (also known as `az`).
> More information: <https://learn.microsoft.com/cli/azure/devops>.

- Set the Personal Access Token (PAT) to login to a particular organization:

`az devops login --organization {{organization_url}}`

- Open a project in the browser:

`az devops project show --project {{project_name}} --open`

- List members of a specific team working on a particular project:

`az devops team list-member --project {{project_name}} --team {{team_name}}`

- Check the Azure DevOps CLI current configuration:

`az devops configure --list`

- Configure the Azure DevOps CLI behavior by setting a default project and a default organization:

`az devops configure --defaults project={{project_name}} organization={{organization_url}}`
