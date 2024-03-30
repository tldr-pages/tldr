# kops

> Create, destroy, upgrade and maintain Kubernetes clusters.
> More information: <https://github.com/kubernetes/kops/>.

- Create a cluster from the configuration specification:

`kops create cluster -f {{cluster_name.yaml}}`

- Create a new SSH public key:

`kops create secret sshpublickey {{key_name}} -i {{~/.ssh/id_rsa.pub}}`

- Export the cluster configuration to the `~/.kube/config` file:

`kops export kubecfg {{cluster_name}}`

- Get the cluster configuration as YAML:

`kops get cluster {{cluster_name}} -o yaml`

- Delete a cluster:

`kops delete cluster {{cluster_name}} --yes`

- Validate a cluster:

`kops validate cluster {{cluster_name}} --wait {{wait_time_until_ready}} --count {{num_required_validations}}`
