# exo compute sks

> Manage the Exoscale Scalable Kubernetes Service (SKS).
> More information: <https://community.exoscale.com/product/compute/containers/>.

- List the supported SKS cluster versions:

`exo compute sks versions`

- Create a new SKS cluster:

`exo compute sks create {{cluster_name}} {{[-z|--zone]}} {{zone}}`

- List all SKS clusters:

`exo compute sks list`

- Generate a Kubernetes kubeconfig file for an SKS cluster that expires in 1800 seconds:

`exo compute sks kubeconfig {{cluster_name|id}} {{user}} --ttl 1800 {{[-z|--zone]}} {{zone}}`

- Create and add a Nodepool containing 3 nodes to an SKS cluster:

`exo compute sks nodepool add {{cluster_name|id}} {{nodepool_name}} --size 3 {{[-z|--zone]}} {{zone}}`

- Remove a Nodepool from an SKS cluster:

`exo compute sks nodepool delete {{cluster_name|id}} {{nodepool_name|id}}`

- Evict a Node from a Nodepool in an SKS cluster:

`exo compute sks nodepool evict {{cluster_name|id}} {{nodepool_name|id}} {{node_name|id}}`

- Enable the Exoscale CSI driver for an existing SKS cluster:

`exo compute sks update {{cluster_name|id}} --enable-csi-addon {{[-z|--zone]}} {{zone}}`
