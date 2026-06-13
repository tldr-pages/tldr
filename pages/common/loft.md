# loft

> Install and manage multi-tenant Kubernetes environments using virtual clusters.
> More information: <https://loft.sh/docs/cli/loft/>.

- Install or upgrade Loft in the current Kubernetes cluster:

`loft start`

- Authenticate to a remote Loft instance:

`loft login {{https://loft.example.com}}`

- Create a virtual cluster with a specific space and cluster:

`loft create vcluster {{vcluster_name}} {{[-s|--space]}} {{space_name}} {{[-c|--cluster]}} {{cluster_name}}`

- List all virtual clusters:

`loft list vclusters`

- Switch context to a specific virtual cluster:

`loft use vcluster {{vcluster_name}}`

- Delete a virtual cluster:

`loft delete vcluster {{vcluster_name}}`

- Show the current Loft username:

`loft vars username`

- Uninstall Loft from the cluster:

`loft uninstall`
