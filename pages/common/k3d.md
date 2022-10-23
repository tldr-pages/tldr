# k3d

> Wrapper CLI to easily create k3s clusters inside docker.
> More information: <https://k3d.io/>.

- Create a cluster:

`k3d cluster create {{cluster_name}}`

- Delete a cluster:

`k3d cluster delete {{cluster_name}}`

- Create a new containerized k3s node:

`k3d node create {{node_name}}`

- Import a image from docker into k3d cluster:

`k3d image import {{image_name}} -c {{cluster_name}}`

- Create a new registry:

`k3d registry create {{registry_name}}`
