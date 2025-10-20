# kubectl kustomize

> Build a set of Kubernetes resources using a `kustomization.yaml` file.
> More information: <https://kubernetes.io/docs/reference/kubectl/generated/kubectl_kustomize/>.

- Build resources from the current directory:

`kubectl kustomize`

- Build resources from a specific directory:

`kubectl kustomize {{path/to/directory}}`

- Build resources from a remote URL:

`kubectl kustomize {{https://github.com/user/repo/path}}`

- Build resources and save to a file:

`kubectl kustomize {{path/to/directory}} > {{output.yaml}}`

- Build resources with load restrictor disabled:

`kubectl kustomize --load-restrictor {{LoadRestrictionsNone}} {{path/to/directory}}`
