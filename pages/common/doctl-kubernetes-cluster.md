# doctl kubernetes cluster

> Manage Kubernetes clusters and view configuration options relating to clusters.
> More information: <https://docs.digitalocean.com/reference/doctl/reference/kubernetes/cluster/>.

- Create a Kubernetes cluster:

`doctl kubernetes cluster create --count {{3}} --region {{nyc1}} --size {{s-1vcpu-2gb}} --version {{latest}} {{cluster_name}}`

- List all Kubernetes clusters:

`doctl kubernetes cluster list`

- Fetch and save the kubeconfig:

`doctl kubernetes cluster kubeconfig save {{cluster_name}}`

- Check for available upgrades:

`doctl kubernetes cluster get-upgrades {{cluster_name}}`

- Upgrade a cluster to a new Kubernetes version:

`doctl kubernetes cluster upgrade {{cluster_name}}`

- Delete a cluster:

`doctl kubernetes cluster delete {{cluster_name}}`
