# eksctl

> The official CLI for Amazon EKS.
> More information: <https://eksctl.io/>.

- Create a basic cluster:

`eksctl create cluster`

- List the details about a cluster or all of the clusters:

`eksctl get cluster [--name=<name>][--region=<region>]`

- Create a cluster passing all configuration information in a file using `--config-file`:

`eksctl create cluster --config-file=<path>`

- Create a cluster using a configuration file and skip creating nodegroups until later:

`eksctl create cluster --config-file=<path> --without-nodegroup`

- Delete a cluster:

`eksctl delete cluster --name=<name> [--region=<region>]`

- Create cluster and write cluster credentials to a file other than default:

`eksctl create cluster --name=cluster-2 --nodes=4 --kubeconfig=./kubeconfig.cluster-2.yaml`

- Create a cluster and prevent storing cluster credentials locally:

`eksctl create cluster --name=cluster-3 --nodes=4 --write-kubeconfig=false`

- Create a cluster and let eksctl manage cluster credentials under `~/.kube/eksctl/clusters` directory:

`eksctl create cluster --name=cluster-3 --nodes=4 --auto-kubeconfig`
