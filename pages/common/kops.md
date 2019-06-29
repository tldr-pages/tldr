# kops

> A tool that create, destroy, upgrade and maintain production-grade, highly available, Kubernetes clusters from the command line.
> More informations: <https://github.com/kubernetes/kops/>.

- Create a cluster from the configuration specification:

`kops create cluster -f {{my-cluster.yaml}}`

- Create secret from secret spec file:

`kops create -f {{secret.yaml}}`

- Export configurations from a cluster:

`kops export kubecfg {{my-cluster}}`

- Get the cluster configuration as yaml:

`kops get cluster {{my-cluster}} -o yaml`

- Delete cluster:

`kops delete cluster {{my-cluster}} --yes`
