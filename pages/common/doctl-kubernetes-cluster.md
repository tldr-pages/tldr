# doctl kubernetes cluster

> For managing Kubernetes clusters and viewing configuration options relating to clusters.
> More information: <https://docs.digitalocean.com/reference/doctl/reference/kubernetes/>.

- Create a Kubernetes cluster:

`doctl kubernetes cluster create --count {{3}} --region {{nyc1}} --size {{s-1vcpu-2gb}} --version {{latest}} {{cluster-name}}`

- List all Kubernetes clusters:

`doctl kubernetes cluster list`

- Fetch and save the kubeconfig:

`doctl kubernetes cluster kubeconfig save {{cluster-name}}`

- Check for available upgrades:

`doctl kubernetes cluster get-upgrades {{cluster-name}}`

- Upgrade a cluster:

`doctl kubernetes cluster upgrade {{cluster-name}}`

- Delete a cluster:

`doctl kubernetes cluster delete {{cluster-name}}` 
