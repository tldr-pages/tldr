# az repos

> Manage Azure DevOps repos.
> Part of `azure-cli` (also known as `az`).
> More information: <https://learn.microsoft.com/cli/azure/repos>.

- List all repos in a specific project:

`az repos list --project {{project_name}}`

- Add policy on a specific branch of a specific repository to restrict basic merge:

`az repos policy merge-strategy create --repository-id {{repository_id_in_repos_list}} --branch {{branch_name}} --blocking --enabled --allow-no-fast-forward false --allow-rebase true --allow-rebase-merge true --allow-squash true`

- Add build validation on a specific repository, using an existing build pipeline, to be triggered automatically on source update:

`az repos policy build create --repository-id {{repository_id}} --build-definition-id {{build_pipeline_id}} --branch main --blocking --enabled --queue-on-source-update-only true --display-name {{name}} --valid-duration {{minutes}}`

- List all active Pull Requests on a specific repository within a specific project:

`az repos pr list --project {{project_name}} --repository {{repository_name}} --status active`
