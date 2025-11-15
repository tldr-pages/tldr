# helm

> A package manager for Kubernetes.
> Some subcommands such as `install` have their own usage documentation.
> More information: <https://helm.sh/docs/helm/>.

- Create a helm chart:

`helm create {{chart_name}}`

- Add a new helm repository:

`helm repo add {{repository_name}}`

- List helm repositories:

`helm repo {{[ls|list]}}`

- Update helm repositories:

`helm repo {{[up|update]}}`

- Delete a helm repository:

`helm repo {{[rm|remove]}} {{repository_name}}`

- Install a helm chart:

`helm install {{name}} {{repository_name}}/{{chart_name}}`

- Download helm chart as a tar archive:

`helm get {{chart_release_name}}`

- Update helm dependencies:

`helm {{[dep|dependency]}} {{[up|update]}}`
