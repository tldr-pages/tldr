# helm repo

> Add, list, update and remove helm chart repositories.
> More information: <https://helm.sh/docs/helm/helm_repo/>.

- Add a chart repository:

`helm repo add {{repository_name}} {{https://example.com/charts}}`

- Add a chart repository that requires credentials:

`helm repo add {{repository_name}} {{https://example.com/charts}} --username {{username}} --password {{password}}`

- Add a chart repository, overwriting it if it already exists:

`helm repo add {{repository_name}} {{https://example.com/charts}} --force-update`

- List chart repositories:

`helm repo {{[ls|list]}}`

- List chart repositories in JSON format:

`helm repo {{[ls|list]}} {{[-o|--output]}} json`

- Update the local information about charts from all repositories:

`helm repo {{[up|update]}}`

- Update the local information about charts from a specific repository:

`helm repo {{[up|update]}} {{repository_name}}`

- Remove a chart repository:

`helm repo {{[rm|remove]}} {{repository_name}}`
