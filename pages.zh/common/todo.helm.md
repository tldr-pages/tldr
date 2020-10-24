# helm

> Helm is a package manager for Kubernetes.
> More information: <https://helm.sh/>.

- Create a helm chart:

`helm create {{chart_name}}`

- Add a new helm repository:

`helm repo add {{repo_name}}`

- List helm repositories:

`helm repo list`

- Update helm repositories:

`helm repo update`

- Delete a helm repository:

`helm repo remove {{repo_name}}`

- Install a helm chart:

`helm install {{repo_name}}/{{chart_name}}`

- Download helm chart as a tar archive:

`helm get {{chart_release_name}}`

- Update helm dependencies:

`helm dependency update`
