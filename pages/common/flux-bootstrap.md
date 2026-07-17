# flux bootstrap

> Bootstrap Flux on a Kubernetes cluster.
> More information: <https://fluxcd.io/flux/cmd/flux_bootstrap/>.

- Bootstrap using a GitHub repository:

`flux bootstrap github --owner {{owner}} --repository {{repository}} --path {{path/to/cluster_directory}} --personal`

- Bootstrap using a GitLab repository:

`flux bootstrap gitlab --owner {{owner}} --repository {{repository}} --path {{path/to/cluster_directory}}`

- Bootstrap from a generic Git repository via SSH:

`flux bootstrap git --url {{ssh://git@example.com/repository.git}} --branch {{main}} --path {{path/to/cluster_directory}}`
